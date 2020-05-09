<template>
  <div ref="Container">
    <User :userid="this.UID" :pic="this.PIC" :name="this.NAME" v-if="isLoaded" />
    <CCardGroup columns class="card-columns">
      <RadarChart :userid="this.UID" v-if="isLoaded" />
      <LineChart :userid="this.UID" v-if="isLoaded" />
    </CCardGroup>
  </div>
</template>

<script>
import RadarChart from "../components/Charts/Radar";
import LineChart from "../components/Charts/Line";
import User from "../components/User";
export default {
  components: {
    User: User,
    RadarChart: RadarChart,
    LineChart: LineChart
  },
  data() {
    return {
      loading: true,
      UID: null,
      NAME: null,
      PIC: null,
      isLogin: false,
      isClient: false
    };
  },

  computed: {
    isLoaded: function() {
      // eslint-disable-next-line no-prototype-builtins
      if (this.hasOwnProperty("UID") && this.UID != null) {
        return true;
      }
      return false;
    }
  },

  methods: {
    initLiff: function() {
      let loader = this.$loading.show({
        // Optional parameters
        container: this.fullPage ? null : this.$refs.Container,
        canCancel: false
      });

      window.liff.init(
        {
          liffId: "1654070318-rlnJ7Rpn"
        },
        // eslint-disable-next-line no-unused-vars
        data => {
          if (window.liff.isLoggedIn()) {
            window.liff.getProfile().then(value => {
              console.log(value);
              this.UID = value.userId;
              this.NAME = value.displayName;
              this.PIC = value.pictureUrl;
            });
          } else {
            window.liff.login();
            window.liff.getProfile().then(value => {
              console.log(value);
              this.UID = value.userId;
              this.NAME = value.displayName;
              this.PIC = value.pictureUrl;
            });
          }
          setTimeout(() => {
            loader.hide();
          }, 1500);
        },
        err => {
          console.log("LIFF initialization failed", err);
        }
      );
    }
  },

  created() {
    this.initLiff();
  }
};
</script>

<style>
</style>