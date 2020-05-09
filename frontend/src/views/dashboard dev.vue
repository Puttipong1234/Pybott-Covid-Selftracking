<template>
<div ref="Container">
    <User :userid="this.UID" :pic="this.PIC"/>
    <CCardGroup columns class="card-columns">
      <RadarChart :userid="this.UID"/>
      <LineChart :userid="this.UID"/>
    </CCardGroup>
</div>
</template>

<script>
    
import RadarChart from "../components/Charts/Radar"
import LineChart from "../components/Charts/Line"
import User from "../components/User"
export default {
  components: {
        RadarChart: RadarChart,
        LineChart: LineChart,
        User: User
    },
  data() {
      return {
          loading: true,
          UID: "Ua6a3833011025f912c95b841404c1304",
          NAME: "BOOK",
          PIC: "",
          isLogin: false,
          isClient: false
      }
  },

  methods: {
    initLiff: function(){

      window.liff.init(
        {
          liffId: '1654070318-rlnJ7Rpn'
        },
        data => {
          this.isLogin = window.liff.isLoggedIn()
          if (this.isLogin) {
              window.liff.getProfile().then(value => {
              this.UID = value.userId;
              this.NAME = value.displayName;
              this.PIC = value.pictureUrl;
              console.log(value)
              setTimeout(() => {loader.hide()},2500)
          });
          this.isClient = window.liff.isInClient();
          }
          else {
              window.liff.login();
              window.liff.getProfile().then(value => {
              this.UID = value.userId;
              this.NAME = value.displayName;
              this.PIC = value.pictureUrl;
              console.log(value)
              this.isLogin = true
              this.isClient = window.liff.isInClient();
          });
        }
        },
        err => {
          console.log('LIFF initialization failed', err)
        }
      )
    }
  },

  created: function() {
    // let loader = this.$loading.show({
    //               // Optional parameters
    //               container: this.fullPage ? null : this.$refs.Container,
    //               canCancel: false,
    //   });

    // setTimeout(() => {loader.hide()},2500)

}
}



</script>

<style>

</style>