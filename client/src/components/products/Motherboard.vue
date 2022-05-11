<template>
  <div class="w3-row w3-margin-right">
    <div class="w3-row">
      <div class="w3-card-1">
        <div class="w3-container w3-center">
          <img
            v-if="motherboardData.image_url != 'Placeholder'"
            class="w3-margin-top"
            :src="
              require(`../../assets/products/mb/${motherboardData.image_url}.jpg`)
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
            <img
              class="w3-margin-top"
              :src="
                require(`../../assets/brand_icons/${motherboardData.brands.toLowerCase()}.svg`)
              "
              height="15"
            />
          </p>
          <p>
            {{ $t('components.products.motherboard.description.model') }}:
            {{ motherboardData.model }}
          </p>
          <p v-if="!short">
            {{ $t('components.products.motherboard.description.socket') }}:
            {{ motherboardData.sockets }}
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
      <button v-on:click="select" class="w3-button w3-deep-orange w3-block">
        {{ $t('components.products.graphicsCard.select') }}
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Motherboard',
  props: ['motherboard', 'short', 'id'],
  data () {
    return {
      motherboardData: {},
      products: []
    }
  },
  async created () {
    if (this.id) {
      await axios
        .get('http://127.0.0.1:5000/parts/motherboards', {
          params: { id: this.id }
        })
        .then(r => r.data)
        .then(data => {
          this.motherboardData = data.parts[0]
        })
    } else {
      this.motherboardData = this.motherboard
    }
    this.getProducts()
  },
  methods: {
    select () {
      const payload = {
        filters: {
          motherboard_id: this.motherboardData.id
        }
      }
      this.$store.dispatch('setSelectedMotherboard', this.motherboardData)
      this.$store.dispatch('loadRecommendedBuilds', payload)
    },
    getProducts () {
      const payload = {
        filters: {
          type: 'motherboards',
          part_id: this.motherboardData.id
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
