<template>
  <div class="w3-row w3-margin-right">
    <div class="w3-row">
      <div class="w3-card-1">
        <div class="w3-container w3-center">
          <img
            v-if="processorData.image_url != 'Placeholder'"
            class="w3-margin-top"
            :src="
              require(`../../assets/products/cpu/${processorData.image_url}.jpg`)
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
            <img
              class="w3-margin-top"
              :src="
                require(`../../assets/brand_icons/${processorData.brands.toLowerCase()}.svg`)
              "
              height="15"
            />
          </p>
          <p>
            {{ $t('components.products.processor.description.name') }}:
            {{ processorData.name }}
          </p>
          <p v-if="!short">
            {{ $t('components.products.processor.description.series') }}:
            {{ processorData.cpu_series }}
          </p>
          <p v-if="!short">
            {{ $t('components.products.processor.description.socket') }}:
            {{ processorData.sockets }}
          </p>
          <p v-if="!short">
            {{ $t('components.products.processor.description.memoryType') }}:
            {{ processorData.ram_memory_types }}
          </p>
          <p v-if="!short">
            {{
              $t(
                'components.products.processor.description.maxMemorySupported'
              )
            }}:
            {{ processorData.max_memory_supported }}
          </p>
          <p v-if="!short">
            {{
              $t(
                'components.products.processor.description.integratedGraphicsCard'
              )
            }}:
          </p>
          <p v-if="!short">
            {{ processorData.integrated_graphics || 'Nėra' }}
          </p>
          <p v-if="!short">
            {{
              $t(
                'components.products.processor.description.operatingFrequency'
              )
            }}:
            {{ processorData.operating_frequency_mhz }}
          </p>
          <p v-if="!short">
            {{
              $t('components.products.processor.description.turboFrequency')
            }}:
            {{ processorData.turbo_frequency_mhz }}
          </p>
          <p v-if="!short">
            {{ $t('components.products.processor.description.numberOfCores') }}:
            {{ processorData.number_of_cores }}
          </p>
          <p v-if="!short">
            {{
              $t('components.products.processor.description.numberOfThreads')
            }}:
            {{ processorData.number_of_threads }}
          </p>
          <p>
            {{ $t('components.products.motherboard.description.pricesLabel') }}:
          </p>
          <p v-for="product in products" :key="product">
            {{ product.vendors }} : {{ product.price }}
          </p>
        </div>
      </div>
    </div>
    <div class="w3-row">
      <button v-on:click="select" class="w3-button w3-block w3-deep-orange">
        {{ $t('components.products.graphicsCard.select') }}
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Processor',
  props: ['processor', 'short', 'id'],
  data () {
    return {
      processorData: {},
      products: []
    }
  },
  async created () {
    if (this.id) {
      await axios
        .get('http://127.0.0.1:5000/parts/processors', {
          params: { id: this.id }
        })
        .then(r => r.data)
        .then(data => {
          this.processorData = data.parts[0]
        })
    } else {
      this.processorData = this.processor
    }
    this.getProducts()
  },
  methods: {
    select () {
      const payload = {
        filters: {
          processor_id: this.processorData.id
        }
      }
      this.$store.dispatch('setSelectedProcessor', this.processorData)
      this.$store.dispatch('loadRecommendedBuilds', payload)
    },
    getProducts () {
      const payload = {
        filters: {
          type: 'processors',
          part_id: this.processorData.id
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
