<template>
  <div v-bind:class="bindPowerSupplyClass()">
      <div class="w3-row">
        <div class="w3-card-1">
         <div class="w3-container w3-center">
           <img
              v-if="selectedPowerSupply.image_url && selectedPowerSupply.image_url != 'Placeholder'"
              class="w3-margin-top"
              :src="require(`../../assets/products/psu/${selectedPowerSupply.image_url}.jpg`)"
              height="100"
          >
           <img
              v-else
              class="w3-margin-top"
              src="../../assets/parts/supply.svg"
              height="100"
          >
           <p>
             {{selectedPowerSupply.model || $t('components.parts.powerSupply.notSelected')}}
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
          v-on:click="clear()"
          class="w3-button w3-red w3-block"
        >
          {{$t('components.parts.powerSupply.remove')}}
        </button>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import store from '../../store'
export default {
  name: 'PowerSupply',
  data () {
    return {
      products: []
    }
  },
  async created() {
    this.getProducts()
  },
  computed: {
    selectedPowerSupply: () => store.state.selectedPowerSupply
  },
  methods: {
    bindPowerSupplyClass () {
      if (this.selectedPowerSupply.model) {
        return "w3-row w3-white"
      } else {
        return "w3-row w3-light-grey w3-opacity"
      }
    },
    clear () {
      this.$store.dispatch('clearSelectedPowerSupply')
    },
    getProducts () {
      const payload = {
        'filters': {
          'type': 'pwoer_supplies',
          'part_id': this.selectedPowerSupply.id
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
