var express = require('express')
var app = express()

var exec = require('child_process').exec

var fs = require('fs')

var bodyParser = require('body-parser')
// create application/json parser  
var jsonParser = bodyParser.json()  
// create application/x-www-form-urlencoded parser  
var urlencodedParser = bodyParser.urlencoded({ extended: false })  

var multer  = require('multer')
var storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/')
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname)
  }
})
var upload = multer({ storage: storage })

// 设置跨域访问
app.all('*', function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*")
  res.header("Access-Control-Allow-Headers", "X-Requested-With")
  res.header("Access-Control-Allow-Methods","PUT,POST,GET,DELETE,OPTIONS")
  res.header("X-Powered-By",' 3.2.1')
  // res.header("Content-Type", "application/json;charset=utf-8")
  res.header("Content-Type", "text/html; charset=utf-8")
  next();
});

app.get('/test', function (req, res) {
  var cmdStr = 'cd uploads \n python3 test_suite.py'
  exec(cmdStr, function (err, stdout, stderr) {
    if (err) {
      console.log(err)
    } else {
      // console.log(__dirname)
      // res.send(stdout)
      console.log(stdout)
    }
  })
})

app.get('/HTMLReport.html', function (req, res) {
  res.sendFile( __dirname + "/" + "uploads/HTMLReport.html" );
})

app.use(express.static('public'))
app.get('/index.html', function (req, res) {
  res.sendFile( __dirname + "/" + "index.html" );
})

app.post('/upload', upload.single('file'), function (req, res) {
  fs.readFile(req.file.path, 'utf-8', function (err, content) {
    if (err) {
        res.send(err)
    }
    var data = {
      file: req.file,
      content: content
    }
    res.send(data)
  })
})

app.post('/change', urlencodedParser, function (req, res) {
  // 不知道为什么具体数据跑到了json的key部分而不是value部分
  for (var key in req.body) {
    var data = JSON.parse(key)
  }
  console.log(data)
  fs.writeFile(data.file.path, data.content, function(err) {
    if (err) {
      return console.error(err)
    }
  })
})

var server = app.listen(8081, function () {

  var host = server.address().address
  var port = server.address().port

  console.log("应用实例，访问地址为 http://%s:%s", host, port)

})
