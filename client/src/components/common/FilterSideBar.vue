<template>
  <div class="w3-col">
    <div class="w3-card-4">
      <slot name="componentSelectBar" />
      <div ckass="w3-row" v-for="filter in filters" :key="filter.filter_name">
        <multiselect
          :options="filter.values"
          track-by="id"
          label="name"
          v-model="selectedFilters[filter.filter_name]"
          :selectedLabel="$t('components.common.multiSelect.selectedLabel')"
          :selectLabel="$t('components.common.multiSelect.selectLabel')"
          :deselectLabel="$t('components.common.multiSelect.deselectLabel')"
          :placeholder="$t(`components.common.filters.${filter.filter_name}`)"
        />
      </div>
      <div @click="applyFilters()" class="w3-button w3-black w3-bar">
        {{ $t('components.common.FilterSideBar.applyFilters') }}
      </div>
      <div
        @click="clearFilters()"
        class="w3-button w3-bar"
        style="background-color: #f44336; color: white;"
      >
        {{ $t('components.common.FilterSideBar.clearFilters') }}
      </div>
    </div>
    <div @click="changeLanguage('lt')">
      <country-flag country="lt" size="normal" />
    </div>
    <div @click="changeLanguage('gb')">
      <country-flag country="gb" size="normal" />
    </div>
  </div>
</template>

<script>
import store from '../../store'
import Multiselect from 'vue-multiselect'
export default {
  name: 'FilterSideBar',
  props: ['showPartSelectBar'],
  components: {
    Multiselect
  },
  data () {
    return {
      selectedFilters: {}
    }
  },
  computed: {
    filters: () => store.state.filters,
    selectedPart: () => store.state.selectedPart,
    filterPayload: function () {
      let filterPayload = {}
      for (const filter in this.selectedFilters) {
        filterPayload[filter] = this.selectedFilters[filter].id
      }
      return filterPayload
    }
  },
  methods: {
    applyFilters: function () {
      let payload = {
        filters: this.filterPayload
      }
      if (this.$route.name === 'Builder') {
        payload.selectedPart = this.selectedPart.endpoint
        this.$store.dispatch('loadParts', payload)
      }
    },
    clearFilters: function () {
      this.selectedFilters = {}
      this.applyFilters()
    },
    changeLanguage: function (locale) {
      this.$root.$i18n.locale = locale
    }
  }
}
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
