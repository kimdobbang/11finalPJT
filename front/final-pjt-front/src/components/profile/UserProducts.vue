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
import axios from 'axios';
import { useAccountStore } from '@/stores/accountstore';
import { useProductStore } from '@/stores/productstore';
import { onMounted, ref, computed } from 'vue';
import router from '@/router';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const accountStore = useAccountStore()
const productStore = useProductStore()
const route = useRoute()

const user = ref(accountStore.userNow)
const indexplus = computed(() => {
  return user.value.fixed.length
})

const chartCanvas = ref(null);

onMounted(() => {
  // Access the canvas element using the ref
  const ctx = chartCanvas.value.getContext('2d');

  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
});
</script>

<style scoped>

</style>