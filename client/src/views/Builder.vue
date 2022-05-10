<template>
  <div>
    <div class="w3-row">
      <div class="w3-col s12 m12 l2">
        <PartSideBar/>
      </div>
      <div class="w3-col s12 m12 l8">
        <PartTable/>
      </div>
      <div class="w3-col s12 m12 l2">
        <FilterSideBar ref="filterSideBar">
          <template v-slot:componentSelectBar>
            <PartSelectBar @changed="this.$refs.filterSideBar.clearFilters()"/>
          </template>
        </FilterSideBar>
      </div>
    </div>
  </div>
</template>

<script>
import PartSideBar from '@/components/parts/PartSideBar.vue'
import PartTable from '@/components/parts/PartTable'
import FilterSideBar from '@/components/common/FilterSideBar.vue'
import PartSelectBar from '@/components/parts/PartSelectBar.vue'
export default {
  name: 'Builder',
  components: {
    PartSideBar,
    PartTable,
    FilterSideBar,
    PartSelectBar
  },
  mounted () {
    let initialPayload = {
      'selectedPart': 'processors'
    }
    this.$store.dispatch('loadParts', initialPayload)
  }
}
</script>
