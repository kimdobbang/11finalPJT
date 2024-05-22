<template>
  <div style="display: flex; flex-direction: row;">
      <div>
        <input type="radio" v-model="bankType" value="1" checked/>1금융권 <br>
        <input type="radio" v-model="bankType" value="2" />저축은행
      </div>
      <div>
        <label for="bank">은행 선택 : </label>
        <select v-model="bankName" id="bank">
          <option value="" selected>전체</option>
          <option >123</option>
        </select>
      </div>
      <div v-if="bankType > 1">
        {{ rateType }}
        <input type="radio" v-model="rateType" value="단리" checked/>단리 <br>
        <input type="radio" v-model="rateType" value="복리" />복리 <br>
      </div>
      <button @click="searchClick">검색</button>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/productstore';
import { ref } from 'vue';

const props = defineProps({
  productType:Number
})
const productType = ref(props.productType)
const productStore = useProductStore()
const bankType = ref('')
const bankName = ref('')
const rateType = ref('')

const emit = defineEmits(['searchClick'])
const searchClick = function () {
  emit("searchClick", bankType.value, bankName.value, rateType.value)
  console.log(bankType.value,bankName.value,rateType.value)
}
// console.log(productStore.fixedList.groupby(({kor_co_nm}) => kor_co_nm))
const allList = ref([])
if (productType.value === 1) {
  allList.value = productStore.fixedList
} else {
  allList.value = productStore.installmentList
}
const groupBy = (array, key) => {
            return array.reduce((result, currentValue) => {
                // 키에 해당하는 값 추출
                const groupKey = currentValue[key];
                // 해당 키에 대한 그룹이 없으면 초기화
                if (!result[groupKey]) {
                    result[groupKey] = [];
                }
                // 해당 그룹에 현재 값 추가
                result[groupKey].push(currentValue);
                return result;
            }, {});
        };
const groupedList = groupBy(allList.value, 'kor_co_nm')
console.log(groupedList)
</script>

<style scoped>

</style>