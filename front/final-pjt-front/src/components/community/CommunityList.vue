<template>

  <div style="align-self: flex-end; margin-right: 10%;">
    <RouterLink :to="{name: 'articlecreate'}" class="btn btn-outline-dark mb-1 float-right">글쓰기</RouterLink>
  </div>

  <div class="d-flex flex-column justify-content-center align-items-center text-center" style="width: 80%;">
    <table class="table table-striped text-center" style="border-radius: 5px;">
      <thead>
        <tr>
          <th>번호</th>
          <th>제목</th>
          <th>내용</th>
        </tr>
      </thead>
      <tbody>
        <CommunityListItem 
        v-for="article in communityStore.articles"
        :article = "article"/>
      </tbody>
    </table>  
  
  
  </div>
</template>

<script setup>
import CommunityListItem from '@/components/community/CommunityListItem.vue'
import {onMounted, ref} from 'vue'
import { useCommunityStore } from '@/stores/communitystore'
import { RouterLink } from 'vue-router';
const communityStore = useCommunityStore()

onMounted(() => {
  communityStore.getArticles()
})
</script>

<style scoped>
* {
  font-family: 'Orbit-Regular';
  font-size: 18px;
}
table {
  border-collapse: collapse;
  box-shadow: 4px 4px 10px 0 rgba(0, 0, 0, 0);
}
table.sortable thead {
    font-weight: bold;
    cursor: pointer;
}
th {
  background-color:  rgba(0, 0, 0, 0.792);
  color: whitesmoke;
}
tbody tr:nth-child(even) {
  background-color: #B4BDFF;
}
.write {
  display: flex;
  margin-right: auto;
}
</style>