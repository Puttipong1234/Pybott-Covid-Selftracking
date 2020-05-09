<template>
    <div>
        <CCard>
            <CCardHeader>
                <span class="strong display-6">ข้อมูลผู้ใช้งาน</span>
                <div class="card-header-actions">
                    <div class="text-center">
                        <CIcon
                            name="cilUser"
                            height="24"
                            alt="Logo"
                            v-c-popover="{
                    header: 'Info',
                    content: `ข้อมูลอ้างอิงจาก Account ผู้ใช้งาน Line`,
                    placement: 'bottom-end',
                    }"
                            class="text-warning"
                        />
                    </div>
                </div>
            </CCardHeader>
            <CRow>
                <CCol>
                    <CRow class="my-3 align-items-center justify-content-center ">
                        <CCol class="ml-4 p-0 mt-3">
                            <img
                            :src="this.pic"
                            class="rounded-circle mx-auto d-block"
                            width="97"
                            height="97"
                        />
                            <div class="mt-4 col-sm-12 text-center mx-auto text-danger bold">รหัสผู้ใช้งาน</div>
                        <div class="text-wrap text-center userid mx-auto" style="width: 8rem;">
                            <small>{{this.userid}}</small>
                        </div>
                        </CCol>
                        <CCol class="pl-1 border-left">
                        <div class="mt-4 col-sm-12 small text-grey">| ชื่อผู้ใช้งาน :</div>
                        <div class="col-sm-12 strong"><dt>{{this.name}}</dt></div>

                        <div class="col-sm-12 mt-3 small text-grey">| วันที่เริ่มบันทึก :</div>
                        <div class="col-sm-12 strong">
                            <dt>{{this.joined_date}}</dt>
                        </div>
                        <div class="col-sm-12 mt-3 small text-grey">ความเสี่ยงต่อการติดเชื้อ :</div>
                        <div class="col-sm-12 small">
                            <p :class="classObject" >{{this.status}}</p>
                            <p :class="classObject">ค่าเฉลี่ยอยู่ที่ : {{Number(this.risk).toFixed(2)}}</p>
                        </div>
                        </CCol>
                    </CRow>
                </CCol>
            </CRow>
        </CCard>
        <CCardGroup class="mb-4">
      <CWidgetProgressIcon
        :header="`บันทึกอาการไปแล้ว ${this.history} วัน`"
        text="เป้าหมาย 14 วัน"
        color="danger"
        :value="cal_percent(this.history)"
      >
        <CIcon name="cil-speedometer" height="50" class="text-danger"/>
      </CWidgetProgressIcon>
              // eslint-disable-next-line vue/no-parsing-error
              </CCardGroup class="mb-4">

            <!-- <CCardGroup columns class="card-columns">
      <RadarChart :userid="this.userid"/>
      <LineChart :userid="this.userid"/>
    </CCardGroup> -->


    </div>
</template>

<script>
import axios from "axios"
// import RadarChart from "../components/Charts/Radar"
// import LineChart from "../components/Charts/Line"
export default {
    name: "User",
    props: {
        userid: {
            type: String ,
        },
        pic: {
            type: String ,
        },
        name: {
            type: String ,
        }
    },
      components: {

    },

    methods : {

        cal_percent: function(x){
            return (x*100/14)
        },
        
        avg_score: function(list){

            var total = 0;
                for(var i = 0; i < list.length; i++) {
                    total += list[i];
                }
                var avg = total / list.length;
                if(avg >= 51){
                    this.classObject = "strong text-danger mb-0"
                    return {"avg":avg , "advise" : "ควรกักตัวอยู่ที่บ้านนะคะ"}
                }
                else if(avg >= 21){
                    this.classObject = "strong text-warning mb-0"
                    return {"avg":avg , "advise" : "มีความเสี่ยงปานกลาง"}
                }
                else {
                    this.classObject = "strong text-info mb-0"
                    return {"avg":avg , "advise" : "มีความเสี่ยงต่ำ"}
                }
        },

        get_thai_date: function(date){
            var monthNamesThai = ["มกราคม","กุมภาพันธ์","มีนาคม","เมษายน","พฤษภาคม","มิถุนายน",
                                "กรกฎาคม","สิงหาคม","กันยายน","ตุลาคม","พฤษจิกายน","ธันวาคม"];

            var dayNames = ["วันอาทิตย์ที่","วันจันทร์ที่","วันอังคารที่","วันพุทธที่","วันพฤหัสบดีที่","วันศุกร์ที่","วันเสาร์ที่"];

            var d = new Date(date);

            return(dayNames[d.getDay()]+" "+d.getDate()+" "+monthNamesThai[d.getMonth()]+" "+d.getFullYear());
        },
        
        initdata : function(uid) {
            console.log(uid)
        var url = `https://pybott-6th.herokuapp.com/api/get_user_report/`+uid
        console.log(url)
    axios
      .get(url)
      .then(response => {
        this.image = response.data.user_data.PROFILE_PIC
        this.display = response.data.user_data.DISPLAY_NAME
        this.joined_date = Object.keys(response.data.data)[0]
        this.history = response.data.days

        var list = []
        const values = Object.values(response.data.data)
        for (const key in values) {
            if (values.hasOwnProperty(key)) {
                list.push(values[key].score);
            }
        }

        var res = this.avg_score(list)
        this.risk = res.avg
        this.status = res.advise
        this.joined_date = this.get_thai_date(this.joined_date)

      })
      .catch(error => {
        console.log(error)
        this.errored = true
      })
      .finally(() => this.loading = false)
  }
    },

    watch:{

        userId:function (userId) {
            // let loader = this.$loading.show({
            //       // Optional parameters
            //       container: this.fullPage ? null : this.$refs.Container,
            //       canCancel: false,
            // });
            console.log("User : " + userId)
            this.initdata(userId)
            // setTimeout(() => {loader.hide()},1000)
        }
    },

    created(){
        this.initdata(this.userid)
    },

    data() {
        return {
            image: "https://cdn.pixabay.com/photo/2016/08/08/09/17/avatar-1577909_960_720.png",
            display: "ไม่พบข้อมูลผู้ใช้งาน",
            joined_date: "ไม่พบข้อมูลผู้ใช้งาน",
            status: "ไม่พบข้อมูลผู้ใช้งาน",
            risk: "ไม่พบข้อมูลผู้ใช้งาน",
            history: 0, 
            classObject: "strong"
        };
    },
};
</script>

<style lang="scss" scoped>
.userid{
    margin-left :30px;
}
</style>