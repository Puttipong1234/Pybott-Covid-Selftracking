<template>
<CContainer>
    <CCard>
        <CCardHeader>
            สรุปอาการของ
            <span class="strong text-danger">ผู้ใช้งานทั้งหมด</span>
            <div class="card-header-actions">
                <div class="text-center">
                    <CIcon
                        name="cilLightbulb"
                        height="24"
                        alt="Logo"
                        v-c-popover="{
                    header: 'Info',
                    content: `ไม่มีความเสี่ยง(0-10)', 'มีความเสี่ยงเล็กน้อย(11-30)', 'มีความเสี่ยงปานกลาง(31-50)','สุ่มเสี่ยงต่อการติดเชื้อ(51-100)`,
                    placement: 'top-end',
                    }"
                        class="text-warning"
                    />
                </div>
            </div>
        </CCardHeader>
        <CCardBody>
            <CChartDoughnut
                :datasets="defaultDatasets"
                :labels="['ไม่มีความเสี่ยง', 'เสี่ยงเล็กน้อย', 'เสี่ยงปานกลาง','สุ่มเสี่ยง']"
            />
            <p class="text-muted text-center mt-4">
                ข้อมูลจากการบันทึกทั้งหมดที่ผ่านมา <br>ตั้งแต่วันที่ <span class="text-info">4 เมษายน 2020</span>
            </p>
        </CCardBody>

    </CCard>
    </CContainer>
</template>

<script>
import { CChartDoughnut } from "@coreui/vue-chartjs";

export default {
    name: "CChartDoughnutExample",
    components: { CChartDoughnut },
    props:{
        datasample: {
            type:Object
        }
    },

    data(){
        return{
            data : []
        }
    },

    created(){
        this.data.push(this.datasample.a)
        this.data.push(this.datasample.b)
        this.data.push(this.datasample.c)
        this.data.push(this.datasample.d)
    },

    computed: {
        defaultDatasets() {
            return [
                {
                    backgroundColor: [
                        "grey",
                        "#414141",
                        "#af0404",
                        "#ff0000"
                    ],
                    data: this.data
                }
            ];
        },
    }
};
</script>
