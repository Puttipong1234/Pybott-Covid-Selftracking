<template>
    <CHeader fixed with-subheader light class="justify-content-center ">
        <CHeaderBrand class="d-lg-none my-0" to="/">
            <h4 class="display-6 ">PYBOTT <span class="strong text-danger "> COVID-19</span> TRACKER</h4>
        </CHeaderBrand>
        <CSubheader class="px-3">
            <CContainer class="mb-1 mt-2">
                <CRow class="justify-content-center ">
                    <CCol class=" border-right ">
                        <CRow class="justify-content-center ">
                        <CIcon name="cilUser" height="24" alt="Logo" />
                        </CRow>
                        <CRow class="justify-content-center  mt-2">
                            <router-link to="/dashboard">
                        <h6 class="text-dark">Your Report</h6>
                        </router-link>
                        </CRow>
                    </CCol>
                    
                    <CCol class="">
                        <CRow class="justify-content-center">
                        <CIcon name="cilChartPie" height="24" alt="Logo" />
                        </CRow>
                        <CRow class="justify-content-center  mt-2 ">
                             <router-link to="/Polls">
                        <h6 class="text-dark">Polls</h6>
                        </router-link>
                        </CRow>
                    </CCol>
                </CRow>
            </CContainer>
        </CSubheader>
    </CHeader>
</template>

<script>
export default {
    name: "TheHeader",
    components: {}
};
</script>
