<template>
  <div>
    <div class="w3-row">
      <div class="w3-col s12 m12 l2">
        <PartSideBar />
      </div>
      <div class="w3-col s12 m12 l8"></div>
    </div>
  </div>
</template>

<script>
import PartSideBar from '@/components/parts/PartSideBar.vue'
export default {
  name: 'Api',
  components: {
    PartSideBar
  }
}
</script>
