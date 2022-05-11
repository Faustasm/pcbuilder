<template>
  <div class="w3-row w3-margin-right">
    <div class="w3-row">
      <div class="w3-card-1">
        <div class="w3-container w3-center">
          <img
            v-if="graphicsCardData.image_url != 'Placeholder'"
            class="w3-margin-top"
            :src="
              require(`../../assets/products/gpu/${graphicsCardData.image_url}.jpg`)
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
            <img
              class="w3-margin-top"
              :src="
                require(`../../assets/brand_icons/${graphicsCardData.brands.toLowerCase()}.svg`)
              "
              height="15"
            />
          </p>
          <p>
            {{ $t('components.products.graphicsCard.description.name') }}:
            {{ graphicsCardData.name }}
          </p>
          <p v-if="!short">
            {{ $t('components.products.graphicsCard.description.model') }}:
            {{ graphicsCardData.model }}
          </p>
          <p v-if="!short">
            {{ $t('components.products.graphicsCard.description.memoryType') }}:
            {{ graphicsCardData.gpu_memory_types }}
          </p>
          <p v-if="!short">
            {{ $t('components.products.graphicsCard.description.memorySize') }}:
            {{ graphicsCardData.memory_size_gb }}
          </p>
          <p>
            {{
              $t('components.products.graphicsCard.description.pricesLabel')
            }}:
          </p>
          <p v-for="product in products" :key="product">
            {{ product.vendor }} : {{ product.price }}
          </p>
        </div>
      </div>
    </div>
    <div class="w3-row">
      <button v-on:click="select" class="w3-button w3-deep-orange w3-block">
        {{ $t('components.products.graphicsCard.select') }}
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'GraphicsCard',
  props: ['graphicsCard', 'short', 'id'],
  data () {
    return {
      graphicsCardData: {},
      products: []
    }
  },
  async created () {
    if (this.id) {
      await axios
        .get('http://127.0.0.1:5000/parts/graphics_cards', {
          params: { id: this.id }
        })
        .then(r => r.data)
        .then(data => {
          this.graphicsCardData = data.parts[0]
        })
    } else {
      this.graphicsCardData = this.graphicsCard
    }
    this.getProducts()
  },
  methods: {
    select () {
      const payload = {
        filters: {
          graphics_card_id: this.graphicsCardData.id
        }
      }
      this.$store.dispatch('setSelectedGraphicsCard', this.graphicsCardData)
      this.$store.dispatch('loadRecommendedBuilds', payload)
    },
    getProducts () {
      const payload = {
        filters: {
          type: 'graphics_cards',
          part_id: this.graphicsCardData.id
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
