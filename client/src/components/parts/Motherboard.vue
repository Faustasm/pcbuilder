<template>
  <div v-bind:class="bindMotherboardClass()">
    <div class="w3-row">
      <div class="w3-card-1">
        <div class="w3-container w3-center">
          <img
            v-if="
              selectedMotherboard.image_url &&
                selectedMotherboard.image_url != 'Placeholder'
            "
            class="w3-margin-top"
            :src="
              require(`../../assets/products/mb/${selectedMotherboard.image_url}.jpg`)
            "
            height="100"
          />
          <img
            v-else
            class="w3-margin-top"
            src="../../assets/parts/motherboard.svg"
            height="100"
          />
          <p>
            {{
              selectedMotherboard.model ||
                $t('components.parts.motherboard.notSelected')
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
        {{ $t('components.parts.motherboard.remove') }}
      </button>
    </div>
  </div>
</template>

<script>
import store from '../../store'
export default {
  name: 'MotherBoard',
  data () {
    return {
      products: []
    }
  },
  computed: {
    selectedMotherboard: () => store.state.selectedMotherboard
  },
  methods: {
    bindMotherboardClass () {
      if (this.selectedMotherboard.model) {
        return 'w3-row w3-white'
      } else {
        return 'w3-row w3-light-grey w3-opacity'
      }
    },
    clear () {
      this.$store.dispatch('clearSelectedMotherboard')
      this.$store.dispatch('getCompatabilityIssues')
      this.$store.dispatch('getCalculatedPowerUsage')
    }
  }
}
</script>
