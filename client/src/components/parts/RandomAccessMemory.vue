<template>
  <div v-bind:class="bindRandomAccessMemory()">
    <div class="w3-row">
      <div class="w3-card-1">
        <div class="w3-container w3-center">
          <img
            v-if="
              selectedRandomAccessMemory.image_url &&
                selectedRandomAccessMemory.image_url != 'Placeholder'
            "
            class="w3-margin-top"
            :src="
              require(`../../assets/products/ram/${selectedRandomAccessMemory.image_url}.jpg`)
            "
            height="100"
          />
          <img
            v-else
            class="w3-margin-top"
            src="../../assets/parts/ram-memory.svg"
            height="100"
          />
          <p>
            {{
              selectedRandomAccessMemory.model ||
                $t('components.parts.randomAccessMemory.notSelected')
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
        {{ $t('components.parts.randomAccessMemory.remove') }}
      </button>
    </div>
  </div>
</template>

<script>
import store from '../../store'
export default {
  name: 'RandomAccessMemory',
  data () {
    return {
      products: []
    }
  },
  computed: {
    selectedRandomAccessMemory: () => store.state.selectedRandomAccessMemory
  },
  methods: {
    bindRandomAccessMemory () {
      if (this.selectedRandomAccessMemory.model) {
        return 'w3-row w3-white'
      } else {
        return 'w3-row w3-light-grey w3-opacity'
      }
    },
    clear () {
      this.$store.dispatch('clearSelectedRandomAccessMemory')
      this.$store.dispatch('getCompatabilityIssues')
      this.$store.dispatch('getCalculatedPowerUsage')
    }
  }
}
</script>
