<template>
  <div class="w3-row">
      <div class="w3-row">
        <div class="w3-card-1">
         <div class="w3-container w3-center">
           <img
              v-if="randomAccessMemoryData.image_url != 'placeholder'"
              class="w3-margin-top"
              :src="require(`../../assets/products/ram/${randomAccessMemoryData.image_url}.jpg`)"
              height="100"
          >
           <img
              v-else
              class="w3-margin-top"
              src="../../assets/parts/ram-memory.svg"
              height="100"
          >
           <p>{{randomAccessMemoryData.brands}}</p>
           <p>
             {{$t('components.products.randomAccessMemory.description.model')}}:
             {{randomAccessMemoryData.model}}
           </p>
           <p v-if="!short">
             {{$t('components.products.randomAccessMemory.description.memoryType')}}:
             {{randomAccessMemoryData.ram_memory_types}}
           </p>
           <p v-if="!short">
             {{$t('components.products.randomAccessMemory.description.casLatency')}}:
             {{randomAccessMemoryData.cas_latency}}
           </p>
           <p v-if="!short">
             {{$t('components.products.randomAccessMemory.description.voltage')}}:
             {{randomAccessMemoryData.voltage}}
           </p>
           <p v-if="!short">
             {{$t('components.products.randomAccessMemory.description.modules')}}:
             {{randomAccessMemoryData.modules}}
           </p>
           <p v-if="!short">
             {{$t('components.products.randomAccessMemory.description.speed')}}:
             {{randomAccessMemoryData.speed}}
           </p>
           <p v-if="!short">
             {{$t('components.products.randomAccessMemory.description.moduleCapacity')}}:
             {{randomAccessMemoryData.module_capacity_gb}}
           </p>
           <p v-if="!short">
             {{$t('components.products.randomAccessMemory.description.capacity')}}:
             {{randomAccessMemoryData.total_capacity_gb}}
           </p>
           <p>
             {{$t('components.products.randomAccessMemory.description.pricesLabel')}}:
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
          v-on:click="select(randomAccessMemory)"
          class="w3-button w3-deep-orange w3-block"
        >
          {{$t('components.products.graphicsCard.select')}}
        </button>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'RandomAccessMemory',
  props: ['randomAccessMemory', 'short', 'id'],
  data () {
    return {
      randomAccessMemoryData: {},
      products: []
    }
  },
  async created() {
    if (this.id) {
      await axios
        .get(
          'http://127.0.0.1:5000/parts/random_access_memory',
          {
            params: {'id': this.id}
          }
        )
        .then(r => r.data)
        .then(data => {
          this.randomAccessMemoryData = data.parts[0]
        })
    } else {
      this.randomAccessMemoryData = this.randomAccessMemory
    }
    this.getProducts()
  },
  methods: {
    select () {
      const payload = {
        'filters': {
          'random_access_memory_id': this.randomAccessMemoryData.id,
          'by_popularity': true
        }
      }
      this.$store.dispatch('setSelectedRandomAccessMemory', this.randomAccessMemoryData)
      this.$store.dispatch('loadRecommendedBuilds', payload)
    },
    getProducts () {
      const payload = {
        'filters': {
          'type': 'processors',
          'part_id': this.randomAccessMemoryData.id
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
