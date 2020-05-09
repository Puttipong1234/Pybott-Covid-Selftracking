<template>
  <div :v-if="this.loading">
    <CCol sm="12" lg="6" class="justify-content-center">
      <CWidgetDropdown
        color="danger"
        :header="`${this.user_num} members`"
        text="ยอดผู้บันทึกอาการ COVID-19 ณ ปัจจุบัน"
      >
        <template #default>
          <CIcon name="cilUser" height="40" class />
        </template>
        <template #footer>
          <CChartBarSimple
            class="mt-3 mx-3"
            style="height: 70px;"
            background-color="rgb(250, 152, 152)"
            label="Members"
            labels="months"
          />
        </template>
      </CWidgetDropdown>
      <CRow class="justify-content-center">
        <DoughnutChart :datasample="this.sample" v-if="isLoaded" />
      </CRow>
    </CCol>
  </div>
</template>

<script>
import DoughnutChart from '../components/Charts/Doughnut'
import CChartBarSimple from '../views/charts/CChartBarSimple'
import axios from 'axios'
export default {
  name: 'WidgetsDropdown',
  components: { DoughnutChart, CChartBarSimple },

  created() {
    this.initdata_sample()
  },

  methods: {
    initdata_sample: function () {
      window.liff.init({ liffId: '1654070318-rlnJ7Rpn' })

      var url = `https://pybott-6th.herokuapp.com/api/get_polls/`
      axios
        .get(url)
        .then((response) => {
          this.user_num = Object.keys(response.data).length
          var a = []
          var b = []
          var c = []
          var d = []

          for (const property in response.data) {
            for (const each in response.data[property]) {
              let data = Number(response.data[property][each].score)
              if (data !== 'null' && data !== 'undefined' && data !== '') {
                if (data <= 10) {
                  a.push(data)
                } else if (11 < data && data <= 30) {
                  b.push(data)
                } else if (31 < data && data <= 50) {
                  c.push(data)
                } else if (51 < data && data <= 100) {
                  d.push(data)
                }
              }
            }
          }

          this.sample.a = a.length
          this.sample.b = b.length
          this.sample.c = c.length
          this.sample.d = d.length
        })
        .catch((error) => {
          console.log(error)
          this.errored = true
        })
        .finally(() => (this.loading = true))
    },
  },
  data() {
    return {
      user_num: 0,
      sample: {
        a: null,
        b: null,
        c: null,
        d: null,
      },
      loading: false,
    }
  },
  computed: {
    isLoaded: function () {
      // eslint-disable-next-line no-prototype-builtins
      if (this.hasOwnProperty('sample') && this.sample.a !== null) {
        return true
      }
      return false
    },
  },
}
</script>

<style></style>
