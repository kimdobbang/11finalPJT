<template>
  <div>
    <h2>가입한 상품들</h2>
    <div v-for="(product, idx) in user.fixed">
      <p>{{ idx + 1 }}. [정기예금] {{ productStore.fixedList[product-1].kor_co_nm }} - {{ productStore.fixedList[product-1].fixed_name }}</p>
    </div>
    <div v-for="(product, idx) in user.installment">
      <p>{{ idx + 1 + indexplus }}. [정기적금] {{ productStore.installmentList[product-1].kor_co_nm }} - {{ productStore.installmentList[product-1].installment_name }}</p>
    </div>
  </div>
  <div>
    <h2>가입한 상품 금리</h2>
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script setup>
import { useRoute,RouterLink } from 'vue-router';
import { useAccountStore } from '@/stores/accountstore';
import { useProductStore } from '@/stores/productstore';
import { onMounted, ref, computed } from 'vue';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const accountStore = useAccountStore()
const productStore = useProductStore()

const user = ref(accountStore.userNow)
const indexplus = computed(() => {
  return user.value.fixed.length
})

const chartCanvas = ref(null);

const Utils = {
  CHART_COLORS: {
    red: 'rgb(255, 99, 132)',
    blue: 'rgb(54, 162, 235)',
    // 다른 색상도 필요하면 추가하세요.
  },
  transparentize: (color, opacity) => {
    const alpha = opacity === undefined ? 0.5 : 1 - opacity;
    return color.replace('rgb(', 'rgba(').replace(')', `, ${alpha})`);
    }
  }

onMounted(() => {
  const ctx = chartCanvas.value.getContext('2d');

  const fixedArray = user.value.fixed.map(id => productStore.fixedList[id-1].fixed_name)

  const installmentArray = user.value.installment.map(id => productStore.installmentList[id-1].installment_name)

  const fixedintrArray = user.value.fixed.map(id => {
  // fixedOptionList에서 product가 id와 같은 첫 번째 객체 찾기
  const fixedOption = productStore.fixedOptions.find(option => option.product === id)
  // 찾은 객체가 있으면 그 객체의 intr 속성 값 반환
  return fixedOption ? fixedOption.intr_rate : 0;
})

const installmentintrArray = user.value.installment.map(id => {
  // fixedOptionList에서 product가 id와 같은 첫 번째 객체 찾기
  const installmentOption = productStore.installmentOptions.find(option => option.product === id)
  // 찾은 객체가 있으면 그 객체의 intr 속성 값 반환
  return installmentOption ? installmentOption.intr_rate : 0;
})

const fixedintr2Array = user.value.fixed.map(id => {
  // fixedOptionList에서 product가 id와 같은 첫 번째 객체 찾기
  const fixedOption = productStore.fixedOptions.find(option => option.product === id)
  // 찾은 객체가 있으면 그 객체의 intr2 속성 값 반환
  return fixedOption ? fixedOption.intr_rate2 : 0;
})

const installmentintr2Array = user.value.installment.map(id => {
  // fixedOptionList에서 product가 id와 같은 첫 번째 객체 찾기
  const installmentOption = productStore.installmentOptions.find(option => option.product === id)
  // 찾은 객체가 있으면 그 객체의 intr2 속성 값 반환
  return installmentOption ? installmentOption.intr_rate2 : 0;
})
  
  const labels = [...fixedArray, ...installmentArray]
  const data = {
    labels: labels,
    datasets: [
      {
        label: '저축 금리',
        data: [...fixedintrArray, ...installmentintrArray],
        borderColor: Utils.CHART_COLORS.blue,
        backgroundColor: Utils.transparentize(Utils.CHART_COLORS.blue, 0.5),
        borderWidth: 2,
        borderRadius: 5,
        borderSkipped: false,
      },
      {
        label: '최고 우대금리',
        data: [...fixedintr2Array, ...installmentintr2Array],
        borderColor: Utils.CHART_COLORS.red,
        backgroundColor: Utils.transparentize(Utils.CHART_COLORS.red, 0.5),
        borderWidth: 2,
        borderRadius: 5,
        borderSkipped: false,
      }
    ]
  };

  new Chart(ctx, {
    type: 'bar',
    data: data,
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: '가입한 상품 금리 비교'
        }
      }
    },
  });
});
</script>

<style scoped>

</style>