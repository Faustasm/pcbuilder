<template>
  <multiselect
    v-model="selectedPart"
    :options="partsListLabeled"
    :placeholder="$t('components.parts.partSelectBar.component')"
    :selectedLabel="$t('components.common.multiSelect.selectedLabel')"
    :selectLabel="$t('components.common.multiSelect.selectLabel')"
    :deselectLabel="$t('components.common.multiSelect.deselectLabel')"
    track-by="endpoint"
    label="label"
    @input="setSelectedPart"
  >
  </multiselect>
</template>

<script>
import store from '../../store'
import Multiselect from 'vue-multiselect'
export default {
  name: 'PartSelectBar',
  componets: [Multiselect],
  computed: {
    selectedPart: function () {
      return {
        endpoint: store.state.selectedPart.endpoint,
        label: this.$t(`components.parts.partSelectBar.${store.state.selectedPart.endpoint}`)
      }
    },
    partsList: () => store.state.partsList,
    partsListLabeled: function () {
      let partsListLabeled = []
      this.partsList.forEach(part => {
        partsListLabeled.push({
          endpoint: part,
          label: this.$t(`components.parts.partSelectBar.${part}`)
        })
      })
      return partsListLabeled
    },
    toCamelCase: function (str) {
      const regExp = /[-_]\w/gi
      return str.replace(regExp, match => {
        return match[1].toUppercase()
      })
    }
  },
  methods: {
    setSelectedPart: function (value) {
      let payload = {
        selectedPart: value.endpoint
      }
      this.$store.dispatch('loadParts', payload)
    }
  }
}
</script>
