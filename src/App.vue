<template>
  <div id="app">
    <el-container>
      <el-header>
        <md-toolbar class="md-dense md-primary">
          <div class="md-toolbar-section-start">
            <md-button class="md-icon-button">
              <md-icon>menu</md-icon>
            </md-button>
          </div>

          <h3 class="md-display-1" style="flex: 1">Testify</h3>

          <div class="md-toolbar-section-end">
            <md-button class="md-icon-button">
              <md-icon>refresh</md-icon>
            </md-button>

            <md-button class="md-icon-button">
              <md-icon>more_vert</md-icon>
            </md-button>
          </div>
        </md-toolbar>
      </el-header>
      <el-main>
        <div class="md-layout md-gutter md-alignment-center">
          <div class="md-layout-item md-size-15">
            <md-field>
              <label>Upload files</label>
              <md-file v-model="placeholder" placeholder="Choose a file" @change="onChange($event)"
              @click="fileclick"/>
            </md-field>
          </div>
          <div class="md-layout-item md-size-15">
            <md-button class="md-raised md-primary" @click="uploadClick">Upload</md-button>
          </div>
        </div>
        <md-button class="md-raised md-primary" @click="test">test</md-button>
        <a href="http://localhost:8081/HTMLReport.html">
        <md-button class="md-raised md-primary">view result</md-button>
        </a>
        <transition name="el-zoom-in-top">
          <myTable v-if="ishow" :msg="upload.content" @change="handleChange"/>
        </transition>
        <router-view/>
      </el-main>
      <el-footer></el-footer>
    </el-container>
  </div>
</template>

<script>
import axios from 'axios'
import myTable from '@/components/table'
import qs from 'qs'

export default {
  name: 'App',
  data () {
    return {
      target_file: '',
      menuVisible: false,
      upload: {
        file: null,
        content: ''
      },
      placeholder: '',
      ishow: false
    }
  },
  components: {
    myTable
  },
  methods: {
    onChange: function (event) {
      this.target_file = event.target.files[0]
    },
    fileclick: function () {
      this.ishow = false
    },
    uploadClick: function () {
      var formData = new FormData()
      formData.append('file', this.target_file)
      // specify Content-Type, with formData as welly
      axios.post('http://localhost:8081/upload', formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
      }).then(response => {
        this.upload.file = response.data.file
        this.upload.content = response.data.content
        this.ishow = true
      }, response => {
        this.$message({
          duration: 1000,
          message: 'server connect error',
          type: 'error'
        })
      })
    },
    test: function () {
      axios.get('http://localhost:8081/test').then(response => {
        console.log(response)
      }, response => {
      })
    },
    viewresult: function () {
      axios.get('http://localhost:8081/viewresult').then(response => {
        
        // console.log(response.data)
      }, response => {
      })
    },
    handleChange: function (data) {
      // 把data数组转为一个string方便后端直接写入文件
      var write = []
      data.forEach(item => {
        write.push([item.Input, item.Output].join(' '))
      })
      this.upload.content = write.join('\n')
      
      var postdata = {
        file: this.upload.file,
        content: this.upload.content
      }

      axios.post('http://localhost:8081/change', postdata, {
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
      }).then(response => {
      }, response => {
        this.$message({
          duration: 1000,
          message: 'server connect error',
          type: 'error'
        })
      })
    }
  }
}
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
small {
  display: block;
}
</style>
