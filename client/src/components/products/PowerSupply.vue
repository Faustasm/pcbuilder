<template>
  <div class="w3-row w3-margin-right">
      <div class="w3-row">
        <div class="w3-card-1">
         <div class="w3-container w3-center">
           <img
              v-if="powerSupplyData.image_url != 'Placeholder'"
              class="w3-margin-top"
              :src="require(`../../assets/products/psu/${powerSupplyData.image_url}.jpg`)"
              height="100"
          >
           <img
              v-else
              class="w3-margin-top"
              src="../../assets/parts/supply.svg"
              height="100"
          >
           <p>{{powerSupplyData.brands}}</p>
           <p>
             {{$t('components.products.powerSupply.description.model')}}:
             {{powerSupplyData.model}}
           </p>
           <p v-if="!short">
             {{$t('components.products.powerSupply.description.maxPower')}}:
             {{powerSupplyData.max_power_w}}
           </p>
           <p v-if="!short">
             {{$t('components.products.powerSupply.description.energyEfficiency')}}:
           </p>
           <p v-if="!short">
             {{powerSupplyData.energy_efficiencies}}
           </p>
           <p v-if="!short">
             {{$t('components.products.powerSupply.description.modularity')}}:
             {{powerSupplyData.modularity}}
           </p>
           <p
              v-for="product in products"
              :key="product"
           >
            {{product.vendor}} : {{product.price}}
          </p>
         </div>
       </div>
      </div>
      <div class="w3-row">
        <button
          v-on:click="select"
          class="w3-button w3-deep-orange w3-block"
        >
          {{$t('components.products.powerSupply.select')}}
        </button>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'PowerSupply',
  props: ['powerSupply', 'short', 'id'],
  data () {
    return {
      powerSupplyData: {},
      products: []
    }
  },
  async created() {
    if (this.id) {
      await axios
        .get(
          'http://127.0.0.1:5000/parts/power_supplies',
          {
            params: {'id': this.id}
          }
        )
        .then(r => r.data)
        .then(data => {
          this.powerSupplyData = data.parts[0]
        })
    } else {
      this.powerSupplyData = this.powerSupply
    }
    this.getProducts()
  },
  methods: {
    select () {
      const payload = {
        'filters': {
          'power_supply_id': this.powerSupplyData.id
        }
      }
      this.$store.dispatch('setSelectedPowerSupply', this.powerSupplyData)
      this.$store.dispatch('loadRecommendedBuilds', payload)
    },
    getProducts () {
      const payload = {
        'filters': {
          'type': 'power_supplies',
          'part_id': this.powerSupplyData.id
        }
      }
      axios
        .get(
          'http://127.0.0.1:5000/products',
          {
            params: payload.filters
          }
        )
        .then(r => r.data)
        .then(data => {
          this.products = data.products
        })
    }
  }
}
</script>
