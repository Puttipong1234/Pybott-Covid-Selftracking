<template>
  <CRow>
    <CCol sm="4" lg="2">
      <CWidgetSimple header="title" text="1,123">
        <CChartLineSimple style="height:40px" border-color="danger" />
      </CWidgetSimple>
    </CCol>
  </CRow>
</template>

<script>
import { CChartLineSimple } from "../Charts/CChartLineSimple";
import { CChartBarSimple } from "../Charts/CChartBarSimple";
export default {
  name: "symtonCard",
  // eslint-disable-next-line vue/no-unused-components
  components: { CChartLineSimple, CChartBarSimple }
};
</script>

<style>
</style>