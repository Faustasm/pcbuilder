<template>
  <div>
    <div class="w3-row">
      <div class="w3-col s12 m12 l2">
        <PartSideBar />
      </div>
      <div class="w3-col s12 m12 l8">
        <BuildTable />
      </div>
      <div class="w3-col s12 m12 l2">
        <FilterSideBar />
      </div>
    </div>
  </div>
</template>

<script>
import PartSideBar from '@/components/parts/PartSideBar.vue'
import BuildTable from '@/components/builds/BuildTable'
import FilterSideBar from '@/components/common/FilterSideBar.vue'
export default {
  name: 'RecommendationSystem',
  components: {
    PartSideBar,
    BuildTable,
    FilterSideBar
  },
  mounted () {
    let initialPayload = {
      filters: {}
    }
    this.$store.dispatch('loadBuilds', initialPayload)
  }
}
</script>
