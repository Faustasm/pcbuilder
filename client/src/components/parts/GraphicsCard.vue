<template>
  <div v-bind:class="bindGraphicsCardClass()">
    <div class="w3-row">
      <div class="w3-card-1">
        <div class="w3-container w3-center">
          <img
            v-if="
              selectedGraphicsCard.image_url &&
                selectedGraphicsCard.image_url != 'Placeholder'
            "
            class="w3-margin-top"
            :src="
              require(`../../assets/products/gpu/${selectedGraphicsCard.image_url}.jpg`)
            "
            height="100"
          />
          <img
            v-else
            class="w3-margin-top"
            src="../../assets/parts/gpu.svg"
            height="100"
          />
          <p>
            {{
              selectedGraphicsCard.name ||
                $t('components.parts.graphicsCard.notSelected')
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
        {{ $t('components.parts.graphicsCard.remove') }}
      </button>
    </div>
  </div>
</template>

<script>
import store from '../../store'
export default {
  name: 'GraphicsCard',
  data () {
    return {
      products: []
    }
  },
  computed: {
    selectedGraphicsCard: () => store.state.selectedGraphicsCard
  },
  methods: {
    bindGraphicsCardClass () {
      if (this.selectedGraphicsCard.name) {
        return 'w3-row w3-white'
      } else {
        return 'w3-row w3-light-grey w3-opacity'
      }
    },
    clear () {
      this.$store.dispatch('clearSelectedGraphicsCard')
      this.$store.dispatch('getCompatabilityIssues')
      this.$store.dispatch('getCalculatedPowerUsage')
    }
  }
}
</script>
