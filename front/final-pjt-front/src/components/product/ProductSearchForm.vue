<template>
  <div class="d-flex justify-content-between w-50">
      <div>
        <input type="radio" class="btn-check" name='fingrp' autocomplete="off" id="fingrp1" v-model="bankType" value="1" checked/>
        <label class="btn btn-outline-success" for="fingrp1">1금융권</label>
        <input type="radio" class="btn-check" name='fingrp' autocomplete="off" id="fingrp2" v-model="bankType" value="2" />
        <label class="btn btn-outline-success" for="fingrp2">저축은행</label>
      </div>
      <div v-if="bankType < 2">
        <label for="bank">은행 선택 : </label>
        <select id="bank" @change="bankNameChange($event.target.value)">
          <option value="" selected>전체</option>
          <option v-for="(bank, index) in groupedList" :key="index">{{ bank }}</option>
        </select>
      </div>
      <div v-if="bankType > 1">
        <input type="radio" class="btn-check" name="options-outlined" autocomplete="off" id="Srate" v-model="rateType" value="단리" checked>
        <label class="btn btn-outline-success" for="Srate">단리</label>

        <input type="radio" class="btn-check" name="options-outlined" autocomplete="off" id="Mrate" v-model="rateType" value="복리">
        <label class="btn btn-outline-success" for="Mrate">복리</label>
      </div>
      <button @click="searchClick">검색</button>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/productstore';
import { ref, watch, watchEffect } from 'vue';

const props = defineProps({
  productType: Number
});

const productStore = useProductStore();
const bankType = ref(1);
const bankName = ref('');
const rateType = ref('');

const allList = ref([]);
const groupedList = ref([]);

const updateGroupedList = () => {
  if (bankType.value < 2) {
    allList.value = productStore.fixedList.filter((product) => product.fin_grp_no === 1);
  } else {
    allList.value = productStore.installmentList.filter((product) => product.fin_grp_no === 1);
  }

  groupedList.value = groupBy(allList.value, 'kor_co_nm', (item) => {
    return item.fin_grp_no === 1;
  });
};

const bankNameChange = (newName) => {
  bankName.value = newName;
};

const emit = defineEmits(['searchClick']);
const searchClick = () => {
  emit("searchClick", bankType.value, bankName.value, rateType.value);
  console.log(bankType.value, bankName.value, rateType.value);
};

const groupBy = (array, key, condition) => {
  return array.reduce((result, currentValue) => {
    const groupKey = currentValue[key];
    if (condition(currentValue)) {
      if (!result.includes(groupKey)) {
        result.push(groupKey);
      }
    }
    return result;
  }, []);
};

// 컴포넌트가 마운트될 때와 bankType, bankName이 변경될 때마다 groupedList 업데이트
watchEffect(() => {
  updateGroupedList();
});

watch(bankType, () => {
  updateGroupedList();
});

watch(bankName, () => {
  updateGroupedList();
});
</script>

<style scoped>

</style>