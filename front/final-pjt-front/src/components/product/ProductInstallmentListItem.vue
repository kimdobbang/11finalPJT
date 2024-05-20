<template>
  <li>
    {{ product.installment_name }}
  </li>
</template>

<script setup>
// import { RouterLink } from 'vue-router';

defineProps({
  product:Object
})
</script>

<style lang="scss" scoped>

</style>