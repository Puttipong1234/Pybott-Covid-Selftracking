<template>
  <CCard>
    <CCardHeader>
      <span class="strong text-danger">เปรียบเทียบแต่ละอาการ</span>กับกลุ่มผู้ใช้งานทั้งหมด (ยังอยู่ในขั้นพัฒนา)
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
    <CCardBody>
      <CChartRadar
        :datasets="defaultDatasets"
        :options="defaultOptions"
        :labels="[
      'มีอาการไอแห้ง', 'มีไข้สูง', 'หายใจเหนื่อยหอบ', 'มีน้ำมูก',
      'เจ็บคอ'
    ]"
      />
    </CCardBody>
  </CCard>
</template>

<script>
import { CChartRadar } from "@coreui/vue-chartjs";
import axios from "axios";
export default {
  name: "CChartRadarExample",
  components: { CChartRadar },
  props: {
    userid: {
      type: String
    }
  },

  created() {
    this.initdata_sample();
    console.log("sampledata" + this.sample);
    this.initdata_user();
    console.log("sampledata" + this.user);
  },

  data() {
    return {
      user: {
        list_น้ำมูกไหล: null,
        list_มีอาการเจ็บคอ: null,
        list_มีอาการไอ: null,
        list_มีไข้: null,
        list_เหนื่อยหอบ: null
      },

      sample: {
        list_น้ำมูกไหล: null,
        list_มีอาการเจ็บคอ: null,
        list_มีอาการไอ: null,
        list_มีไข้: null,
        list_เหนื่อยหอบ: null
      },

      loading: true
    };
  },
  computed: {
    defaultDatasets() {
      return [
        {
          label: "ค่าเฉลี่ยผู้ใช้ทั้งหมด",
          backgroundColor: "rgba(179,181,198,0.2)",
          borderColor: "rgba(179,181,198,1)",
          pointBackgroundColor: "rgba(179,181,198,1)",
          pointBorderColor: "#fff",
          pointHoverBackgroundColor: "#fff",
          pointHoverBorderColor: "rgba(179,181,198,1)",
          tooltipLabelColor: "rgba(179,181,198,1)",
          data: [
            this.sample.list_มีอาการไอ,
            this.sample.list_มีไข้,
            this.sample.list_เหนื่อยหอบ,
            this.sample.list_น้ำมูกไหล,
            this.sample.list_มีอาการเจ็บคอ
          ]
        },
        {
          label: "อาการของท่าน",
          backgroundColor: "rgba(255,99,132,0.2)",
          borderColor: "rgb(255,0,0)",
          pointBackgroundColor: "rgba(255,99,132,1)",
          pointBorderColor: "#fff",
          pointHoverBackgroundColor: "#fff",
          pointHoverBorderColor: "rgba(255,99,132,1)",
          tooltipLabelColor: "rgba(255,99,132,1)",
          data: [
            this.user.list_มีอาการไอ,
            this.user.list_มีไข้,
            this.user.list_เหนื่อยหอบ,
            this.user.list_น้ำมูกไหล,
            this.user.list_มีอาการเจ็บคอ
          ]
        }
      ];
    },
    defaultOptions() {
      return {
        aspectRatio: 1.5
      };
    }
  },
  methods: {
    avg_score: function(list) {
      var total = 0;
      for (var i = 0; i < list.length; i++) {
        if (
          list[i] !== "" &&
          typeof list[i] !== "undefined" &&
          list[i] !== null
        ) {
          total += Number(list[i]);
        }
      }
      var avg = total / list.length;
      if (avg >= 51) {
        return avg;
      } else if (avg >= 21) {
        this.classObject = "strong text-warning mb-0";
        return avg;
      } else {
        this.classObject = "strong text-info mb-0";
        return avg;
      }
    },
    initdata_user: function() {
      var url =
        `https://pybott-6th.herokuapp.com/api/get_user_report/` + this.userid;
      axios
        .get(url)
        .then(response => {
          var list_น้ำมูกไหล = [];
          var list_มีอาการเจ็บคอ = [];
          var list_มีอาการไอ = [];
          var list_มีไข้ = [];
          var list_เหนื่อยหอบ = [];
          const values = Object.values(response.data.data);
          for (const key in values) {
            // eslint-disable-next-line no-prototype-builtins
            if (values.hasOwnProperty(key)) {
              list_น้ำมูกไหล.push(values[key].น้ำมูกไหล);
              list_มีอาการไอ.push(values[key].มีอาการไอ);
              list_มีไข้.push(values[key].มีไข้);
              list_เหนื่อยหอบ.push(values[key].เหนื่อยหอบ);
              list_มีอาการเจ็บคอ.push(values[key].มีอาการเจ็บคอ);
            }
          }
          this.user.list_น้ำมูกไหล = this.avg_score(list_น้ำมูกไหล);
          this.user.list_มีอาการไอ = this.avg_score(list_มีอาการไอ);
          this.user.list_มีไข้ = this.avg_score(list_มีไข้);
          this.user.list_เหนื่อยหอบ = this.avg_score(list_เหนื่อยหอบ);
          this.user.list_มีอาการเจ็บคอ = this.avg_score(list_มีอาการเจ็บคอ);
        })
        .catch(error => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    },

    initdata_sample: function() {
      var url = `https://pybott-6th.herokuapp.com/api/get_polls/`;
      axios
        .get(url)
        .then(response => {
          var list_น้ำมูกไหล = [];
          var list_มีอาการเจ็บคอ = [];
          var list_มีอาการไอ = [];
          var list_มีไข้ = [];
          var list_เหนื่อยหอบ = [];
          for (const property in response.data) {
            for (const each in response.data[property]) {
              list_น้ำมูกไหล.push(response.data[property][each].น้ำมูกไหล);
              list_มีอาการไอ.push(response.data[property][each].มีอาการไอ);
              list_มีไข้.push(response.data[property][each].มีไข้);
              list_เหนื่อยหอบ.push(response.data[property][each].เหนื่อยหอบ);
              list_มีอาการเจ็บคอ.push(
                response.data[property][each].มีอาการเจ็บคอ
              );
            }
          }
          this.sample.list_น้ำมูกไหล = this.avg_score(list_น้ำมูกไหล);
          this.sample.list_มีอาการไอ = this.avg_score(list_มีอาการไอ);
          this.sample.list_มีไข้ = this.avg_score(list_มีไข้);
          this.sample.list_เหนื่อยหอบ = this.avg_score(list_เหนื่อยหอบ);
          this.sample.list_มีอาการเจ็บคอ = this.avg_score(list_มีอาการเจ็บคอ);
        })
        .catch(error => {
          console.log(error);
          this.errored = true;
        })
        .finally(() => (this.loading = false));
    }
  }
};
</script>

<style>
</style>