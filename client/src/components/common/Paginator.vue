<template>
  <div class="w3-bar w3-center">
    <a
      href="#"
      class="w3-button"
      v-on:click="changePage(parseInt(currentPage) - 1)"
      v-if="parseInt(currentPage) !== 1"
    >
      &laquo;
    </a>
    <a
      href="#"
      v-on:click="changePage(page)"
      v-bind:class="bindPaginationClass(page)"
      v-for="page in totalPages"
      :key="page"
    >
      {{ page }}
    </a>
    <a
      href="#"
      class="w3-button"
      v-on:click="changePage(parseInt(currentPage) + 1)"
      v-if="parseInt(currentPage) !== parseInt(totalPages)"
    >
      &raquo;
    </a>
  </div>
</template>
&raquo;
<script>
import store from '../../store'
export default {
  name: 'Paginator',
  componets: [],
  computed: {
    selectedPart: () => store.state.selectedPart,
    selectedFilters: () => store.state.selectedFilters,
    currentPage: () => store.state.currentPage,
    totalPages: () => store.state.totalPages
  },
  methods: {
    bindPaginationClass: function (pageNumber) {
      if (pageNumber == this.currentPage || pageNumber == null) {
        return 'w3-button w3-red'
      } else {
        return 'w3-button'
      }
    },
    changePage: function (pageNumber) {
      let filters = this.selectedFilters || {}
      filters.page = pageNumber
      let payload = {
        filters: filters
      }
      if (this.$route.name === 'Builder') {
        payload.selectedPart = this.selectedPart.endpoint
        this.$store.dispatch('loadParts', payload)
      } else {
        this.$store.dispatch('loadBuilds', payload)
      }
    }
  }
}
</script>
