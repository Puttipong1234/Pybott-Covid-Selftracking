<template>
        <CCard>
            <CCardHeader>
                รายงานอาการของท่าน 
                <span class="strong text-danger">จากการบันทึก </span>ที่ผ่านมา (ยังอยู่ในขั้นพัฒนา)
                <div class="card-header-actions">
                    <div class="text-center">
                        <CIcon
                            name="cilLightbulb"
                            height="24"
                            alt="Logo"
                            v-c-popover="{
                    header: 'Info',
                    content: `รายงานจากการกรอกข้อมูล 14 วันล่าสุดของท่าน`,
                    placement: 'bottom-end',
                    }"
                            class="text-warning"
                        />
                    </div>
                </div>
            </CCardHeader>
            <CCardBody >
                <CChartLine :datasets="defaultDatasets" :labels="this.userdata.date" />
            </CCardBody>
        </CCard>
</template>

<script>
import { CChartLine } from "@coreui/vue-chartjs";
import axios from "axios"
export default {
    name: "CChartLineExample",
    components: { CChartLine },

    props: {
        userid: {
            type: String
        }
    },

    watch:{
        userId:function (userId) {
        console.log("Line : " + userId)
        this.initdata_sample()
        console.log("Line_sampledata" + this.sampledata)
        this.initdata_user(userId)
        this.match_date(this.userdata,this.sampledata)
        }
    },

    created(){

        console.log("Line : " + this.userid)
        this.initdata_sample()
        console.log("Line_sampledata" + this.sampledata)
        this.initdata_user(this.userid)
        this.match_date(this.userdata,this.sampledata)

    },

    // updated(){
    //     this.match_date(this.userdata,this.sampledata)
    // },

    computed: {
        defaultDatasets() {
            return [
                {
                    label: "ความเสี่ยงเฉลี่ยผู้ใช้งาน",
                    backgroundColor: "rgba(179,181,198,1)",
                    data: this.sample.data.slice(0,14),
                    fill: false,
                    
                },
                {
                    label: "ความเสี่ยงของท่าน",
                    backgroundColor: "rgb(255,0,0)",
                    data: this.userdata.data.slice(0,14),
                    fill: false,
                    lineTension:0.5,
                    borderColor: "rgb(255,0,0)"
                }
            ];
        },

        
    },

    methods: {
        avg_score: function(list){
            var total = 0;
                for(var i = 0; i < list.length; i++) {
                    if (list[i]!== "" && typeof list[i] !== 'undefined' && list[i]!== null){
                        total += Number(list[i]);
                    }
                }
                var avg = total / list.length;
                if(avg >= 51){
                    return avg
                }
                else if(avg >= 21){
                    this.classObject = "strong text-warning mb-0"
                    return avg
                }
                else {
                    this.classObject = "strong text-info mb-0"
                    return avg
                }
        },

        initdata_sample : function() {
        var url = `https://pybott-6th.herokuapp.com/api/get_polls/`
    axios
      .get(url)
      .then(response => {


          var sample_list = []

          for (const property in response.data) {
              var each_sample_list = []
            for (const each in response.data[property]) {
                each_sample_list.push(response.data[property][each].score);
                }
              this.sample.date.push(Object.keys(response.data[property]))
              // cal avg
              var sample_avg = this.avg_score(each_sample_list)
              sample_list.push(sample_avg);
            }

            this.sample.data = sample_list
            // for (const property in response.data) {
            //     console.log(Object.keys(response.data[property]))
            //     this.sample.date.push()
            //     }
        
      })
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(() => this.loading = false)
  },

        initdata_user : function(uid) {
        var url = `https://pybott-6th.herokuapp.com/api/get_user_report/`+uid
    axios
      .get(url)
      .then(response => {

        var userdata_list = []

        const values = Object.values(response.data.data)
        for (const key in values) {
            if (values.hasOwnProperty(key)) {
                userdata_list.push(values[key].score);
            }
        }
        this.userdata.data = userdata_list
        this.userdata.date= Object.keys(response.data.data)
      })
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(() => this.loading = false)
  },


        match_date: function(userdata,sampledata){

            let date_label = []
            let user_data = []
            let sample_data = []

            for(var i = 0; i < userdata.length; i++){
                for(var j = 0; j < userdata.length; j++){
                    if(sampledata.date[j] === userdata.date[i]){
                        date_label.push(userdata.date[i])
                        user_data.push(userdata.data[i])
                        sample_data.push(sampledata.data[j])
                    }
                }
            }
            this.chart_label = date_label
            this.sample.data = sample_data
        }


    },

    data() {
        return {
            sample : {
                date:[],
                data:[]
            }
            ,userdata : {
                date:[],
                data:[]
            }
        }
    }
};
</script>

<style scoped>

</style>