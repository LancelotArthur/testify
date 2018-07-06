<template>
  <div style="margin-top: 20px">
    <el-table :data="data" border height="400" stripe
      style="width: 90%;margin: 0 auto;background-color: #efeff4;text-align: left">
      <!-- <el-table-column prop="Index" label="Index" width="60px" align="center">
      </el-table-column> -->
      <el-table-column prop="Input" label="Input">
      </el-table-column>
      <el-table-column prop="Output" label="Output">
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button 
            size="mini" 
            type="primary"
            @click="handleAdd(scope.$index, scope.row)">添加</el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
    <!-- 编辑表单 -->
    <el-dialog title="编辑" :visible.sync="dialogEditVisible" style="text-align: left" width="30%">
      <el-form :model="form">
        <el-form-item label="Input" :label-width="formLabelWidth">
          <el-input v-model="form.input" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="Output" :label-width="formLabelWidth">
          <el-autocomplete class="inline-input" v-model="form.output" clearble
            :fetch-suggestions="querySearch"
            placeholder="请输入内容"
            @select="handleSelect"
          ></el-autocomplete>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogEditVisible = false">取 消</el-button>
        <el-button type="primary" @click="confirmEditClick">确 定</el-button>
      </div>
    </el-dialog>
    <!-- 添加表单 -->
    <el-dialog title="添加" :visible.sync="dialogAddVisible" style="text-align: left" width="30%">
      <el-form :model="form">
        <el-form-item label="Input" :label-width="formLabelWidth">
          <el-input v-model="form.input" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="Output" :label-width="formLabelWidth">
          <el-autocomplete class="inline-input" v-model="form.output" clearble
            :fetch-suggestions="querySearch"
            placeholder="请输入内容"
            @select="handleSelect"
          ></el-autocomplete>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogAddVisible = false">取 消</el-button>
        <el-button type="primary" @click="confirmAddClick">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data () {
    return {
      data: [],
      dialogEditVisible: false,
      dialogAddVisible: false,
      outputs: [],
      form: {
        input: '',
        output: ''
      },
      formLabelWidth: '60px',
      index: null
    }
  },
  props: ['msg'],
  mounted: function () {
    var text = this.msg.split('\n')
    text.forEach((item, index) => {
      var temp = item.split(' ')
      if (isNaN(temp[temp.length - 1])) {
        var input = item.substring(0, item.lastIndexOf(' '))
        var output = temp[temp.length - 1]
      } else {
        input = [temp[0],temp[1],temp[2]].join(' ')
        output = [temp[3],temp[4]].join(' ')
      }
      this.data.push({Input: input, Output: output})
    })
    this.outputs = this.loadAll();
  },
  methods: {
    handleEdit: function (index, row) {
      this.form.input = row.Input
      this.form.output = row.Output
      this.index = index
      this.dialogEditVisible = true
    },
    handleDelete: function (index, row) {
      this.data.splice(index, 1)
      this.$emit('change',this.data)
    },
    handleAdd: function (index, row) {
      this.index = index
      this.dialogAddVisible = true
    },
    querySearch: function (queryString, cb) {
      var outputs = this.outputs
      var results = queryString ? outputs.filter(this.createFilter(queryString)) : outputs
      // 调用 callback 返回建议列表的数据
      cb(results)
    },
    createFilter: function (queryString) {
      return (outputs) => {
        return (outputs.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0)
      }
    },
    handleSelect: function (item) {
      console.log(item)
    },
    loadAll: function () {
      return [
        {'value': 'ValueError'},
        {'value': 'ParaNumError'}
      ]
    },
    confirmEditClick: function () {
      this.data[this.index].Input = this.form.input
      this.data[this.index].Output = this.form.output
      this.$emit('change',this.data)
      this.dialogEditVisible = false
    },
    confirmAddClick: function () {
      this.data.splice(this.index + 1, 0, {Input: this.form.input, Output: this.form.output})
      this.$emit('change',this.data)
      this.dialogAddVisible = false
    }
  }
}
</script>

<style>

</style>
