<template>
  <KakaoMap :lat="37.566826" :lng="126.9786567" @onLoadKakaoMap="onLoadKakaoMap">
    <KakaoMapMarker
      v-for="(marker, index) in markerList"
      :key="marker.key === undefined ? index : marker.key"
      :lat="marker.lat"
      :lng="marker.lng"
      :infoWindow="marker.infoWindow"
      :clickable="true"
      @onClickKakaoMapMarker="onClickMapMarker(marker)"
    />
  </KakaoMap>
</template>

<script setup>
import { onMounted, ref, watch, toRaw } from 'vue'
import { KakaoMap, KakaoMapMarker } from 'vue3-kakao-maps'




const map = ref();
const markerList = ref([]);
const props = defineProps(['keyword']);

const onLoadKakaoMap = (mapRef) => {
  map.value = mapRef;
  searchPlaces(props.keyword);
};

const searchPlaces = (keyword) => {
  if (!keyword) return;

  const ps = new kakao.maps.services.Places();
  ps.keywordSearch(keyword, placesSearchCB);
};

const placesSearchCB = (data, status) => {
  if (status === kakao.maps.services.Status.OK) {
    const bounds = new kakao.maps.LatLngBounds();
    markerList.value = [];

    for (let marker of data) {
      const markerItem = {
        lat: marker.y,
        lng: marker.x,
        infoWindow: {
          content: marker.place_name,
          visible: false
        }
      };
      markerList.value.push(markerItem);
      bounds.extend(new kakao.maps.LatLng(Number(marker.y), Number(marker.x)));
    }

    map.value?.setBounds(bounds);
  }
};

const onClickMapMarker = (markerItem) => {
  if (markerItem.infoWindow?.visible !== null && markerItem.infoWindow?.visible !== undefined) {
    markerItem.infoWindow.visible = !markerItem.infoWindow.visible;
  } else {
    markerItem.infoWindow.visible = true;
  }
};

watch(() => props.keyword, (newKeyword) => {
  if (map.value) {
    searchPlaces(newKeyword);
  }
});
</script>

<style scoped>
#map {
  width: 100%;
  height: 600px;
}
</style>
