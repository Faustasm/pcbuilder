<template>
  <div v-bind:class="bindSelectedDrive()">
    <div class="w3-row">
      <div class="w3-card-1">
        <div class="w3-container w3-center">
          <img
            v-if="
              selectedDrive.image_url &&
                selectedDrive.image_url != 'Placeholder'
            "
            class="w3-margin-top"
            :src="
              require(`../../assets/products/drive/${selectedDrive.image_url}.jpg`)
            "
            height="100"
          />
          <img
            v-else
            class="w3-margin-top"
            src="../../assets/parts/hard-drive.svg"
            height="100"
          />
          <p>
            {{
              selectedDrive.model || $t('components.parts.drive.notSelected')
            }}
          </p>
          <p v-for="product in products" :key="product">
            {{ product.vendors }} : {{ product.price }}
          </p>
        </div>
      </div>
    </div>
    <div class="w3-row">
      <button v-on:click="clear()" class="w3-button w3-red w3-block">
        {{ $t('components.parts.drive.remove') }}
      </button>
    </div>
  </div>
</template>

<script>
import store from '../../store'
export default {
  name: 'Drive',
  data () {
    return {
      products: []
    }
  },
  computed: {
    selectedDrive: () => store.state.selectedDrive
  },
  methods: {
    bindSelectedDrive () {
      if (this.selectedDrive.model) {
        return 'w3-row w3-white'
      } else {
        return 'w3-row w3-light-grey w3-opacity'
      }
    },
    clear () {
      this.$store.dispatch('clearSelectedDrive')
      this.$store.dispatch('getCompatabilityIssues')
      this.$store.dispatch('getCalculatedPowerUsage')
    }
  }
}
</script>
