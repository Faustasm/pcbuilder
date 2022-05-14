<template>
  <div v-bind:class="bindProcessorClass()">
    <div class="w3-row">
      <div class="w3-card-1">
        <div class="w3-container w3-center">
          <img
            v-if="
              selectedProcessor.image_url &&
                selectedProcessor.image_url != 'Placeholder'
            "
            class="w3-margin-top"
            :src="
              require(`../../assets/products/cpu/${selectedProcessor.image_url}.jpg`)
            "
            height="100"
          />
          <img
            v-else
            class="w3-margin-top"
            src="../../assets/parts/cpu.svg"
            height="100"
          />
          <p>
            {{
              selectedProcessor.name ||
                $t('components.parts.processor.notSelected')
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
        {{ $t('components.parts.processor.remove') }}
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import store from '../../store'
export default {
  name: 'Processor',
  data () {
    return {
      products: []
    }
  },
  async created () {
    if (this.selectedProcessor.id && this.products.length === 0) {
      await this.getProducts()
    }
  },
  watch: {
    selectedProcessor (newSelectedProcessor, oldSelectedProcessor) {
      if (
        newSelectedProcessor != oldSelectedProcessor &&
        this.selectedProcessor.id
      ) {
        this.getProducts()
      }
    }
  },
  computed: {
    selectedProcessor: () => store.state.selectedProcessor
  },
  methods: {
    bindProcessorClass () {
      if (this.selectedProcessor.name) {
        return 'w3-row w3-white'
      } else {
        return 'w3-row w3-light-grey w3-opacity'
      }
    },
    clear () {
      this.$store.dispatch('clearSelectedProcessor')
      this.$store.dispatch('getCompatabilityIssues')
      this.$store.dispatch('getCalculatedPowerUsage')
    },
    getProducts () {
      const payload = {
        filters: {
          type: 'processors',
          part_id: this.selectedProcessor.id
        }
      }
      axios
        .get('http://127.0.0.1:5000/products', {
          params: payload.filters
        })
        .then(r => r.data)
        .then(data => {
          this.products = data.products
        })
    }
  }
}
</script>
