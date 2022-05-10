<template>
  <div class="w3-margin-top">
    <div class="w3-row">
      <div class="w3-col s12 m12 l12">
        <Paginator/>
      </div>
    </div>
    <div class="w3-container w3-margin-top">
      <div class="w3-row" v-if="showRecommendedProducts">
        <div class="w3-col s12 m12 l4">
          <div class="w3-container w3-center">
            <p>Dažniausiai renkama kartu: </p>
            <img class="w3-margin-top" src="../../assets/right-arrow-svgrepo-com.svg" height="70">
          </div>
        </div>
        <div v-if="selectedPart.endpoint === 'processors'">
          <div class="w3-col s12 m12 l4">
            <GraphicsCard
              v-if="recommendedBuild"
              :id="recommendedBuild.graphics_card_id"
              :short="true"
            />
          </div>
          <div class="w3-col s12 m12 l4">
            <Motherboard
              v-if="recommendedBuild"
              :id="recommendedBuild.motherboard_id"
              :short="true"
            />
          </div>
        </div>
        <div v-if="selectedPart.endpoint === 'graphics_cards'">
          <div class="w3-col s12 m12 l4">
            <Processor
              v-if="recommendedBuild"
              :id="recommendedBuild.processor_id"
              :short="true"
            />
          </div>
          <div class="w3-col s12 m12 l4">
            <Motherboard
              v-if="recommendedBuild"
              :id="recommendedBuild.motherboard_id"
              :short="true"
            />
          </div>
        </div>
        <div v-if="selectedPart.endpoint === 'drives'">
          <div class="w3-col s12 m12 l4">
            <Motherboard
              v-if="recommendedBuild"
              :id="recommendedBuild.motherboard_id"
              :short="true"
            />
          </div>
          <div class="w3-col s12 m12 l4">
            <RandomAccessMemory
              v-if="recommendedBuild"
              :id="recommendedBuild.random_access_memory_id"
              :short="true"
            />
          </div>
        </div>
        <div v-if="selectedPart.endpoint === 'motherboards'">
          <div class="w3-col s12 m12 l4">
            <Processor
              v-if="recommendedBuild"
              :id="recommendedBuild.processor_id"
              :short="true"
            />
          </div>
          <div class="w3-col s12 m12 l4">
            <RandomAccessMemory
              v-if="recommendedBuild"
              :id="recommendedBuild.random_access_memory_id"
              :short="true"
            />
          </div>
        </div>
        <div v-if="selectedPart.endpoint === 'power_supplies'">
          <div class="w3-col s12 m12 l4">
            <GraphicsCard
              v-if="recommendedBuild"
              :id="recommendedBuild.graphics_card_id"
              :short="true"
            />
          </div>
          <div class="w3-col s12 m12 l4">
            <Processor
              v-if="recommendedBuild"
              :id="recommendedBuild.processor_id"
              :short="true"
            />
          </div>
        </div>
        <div v-if="selectedPart.endpoint === 'random_access_memory'">
          <div class="w3-col s12 m12 l4">
            <Processor
              v-if="recommendedBuild"
              :id="recommendedBuild.processor_id"
              :short="true"
            />
          </div>
          <div class="w3-col s12 m12 l4">
            <PowerSupply
              v-if="recommendedBuild"
              :id="recommendedBuild.power_supply_id"
              :short="true"
            />
          </div>
        </div>
      </div>
      <div class="w3-row">
          <div
            class="w3-col s12 m12 l4"
            v-for="part in parts"
            :key="part.id"
          >
            <Processor
              v-if="selectedPart.endpoint === 'processors'"
              :processor="part"
            />
            <GraphicsCard
              v-if="selectedPart.endpoint === 'graphics_cards'"
              :graphicsCard="part"
              :short="false"
            />
            <Motherboard
              v-if="selectedPart.endpoint === 'motherboards'"
              :motherboard="part"
            />
            <RandomAccessMemory
              v-if="selectedPart.endpoint === 'random_access_memory'"
              :randomAccessMemory="part"
            />
            <Drive
              v-if="selectedPart.endpoint === 'drives'"
              :drive="part"
            />
            <PowerSupply
              v-if="selectedPart.endpoint === 'power_supplies'"
              :powerSupply="part"
            />
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import store from '../../store'
import Paginator from '@/components/common/Paginator'
import Processor from '@/components/products/Processor'
import GraphicsCard from '@/components/products/GraphicsCard'
import Motherboard from '@/components/products/Motherboard'
import RandomAccessMemory from '@/components/products/RandomAccessMemory'
import Drive from '@/components/products/Drive'
import PowerSupply from '@/components/products/PowerSupply'
export default {
  name: 'PartTable',
  data () {
    return {
      recommendedPartsMap: {
        processors: {
          partsToRecommend: ['gpu', 'mb']
        }
      },
      graphicsCard: {
        image_url: '1',
        name: 'GeForce GTX 1660 Super OC ',
        model: 'GV-N166SOC-6GD',
        gpu_memory_types: 'GDDR6',
        memory_size_gb: '6',
        prices: [
          {
            'vendor': '3a.lt',
            'price': '$202.00'
          },
          {
            'vendor': 'vgtushop.lt',
            'price': '212.00'
          }
        ]
      },
      graphicsCardTwo: {
        image_url: '2',
        name: 'GeForce RTX 2060',
        model: 'GV-N2060OC-6GD',
        gpu_memory_types: 'GDDR6',
        memory_size_gb: '6',
        prices: [
          {
            'vendor': '3a.lt',
            'price': '$203.00'
          },
          {
            'vendor': 'vgtushop.lt',
            'price': '213.00'
          }
        ]
      }
    }
  },
  components: {
    Paginator,
    Processor,
    GraphicsCard,
    Motherboard,
    RandomAccessMemory,
    Drive,
    PowerSupply
  },
  computed: {
     selectedPart: () => store.state.selectedPart,
     selectedProcessor: () => store.state.selectedProcessor,
     selectedGraphicsCard: () => store.state.selectedGraphicsCard,
     selectedMotherboard: () => store.state.selectedMotherboard,
     selectedRandomAccessMemory: () => store.state.selectedRandomAccessMemory,
     selectedPowerSupply: () => store.state.selectedPowerSupply,
     selectedDrive: () => store.state.selectedDrive,
     parts: () => store.state.parts,
     recommendedBuild: () => store.state.recommendedBuild,
     showRecommendedProducts () {
      if (this.selectedPart.endpoint == 'processors' && this.selectedProcessor.id && this.recommendedBuild && this.recommendedBuild.id) {
        return true
      }
      if (this.selectedPart.endpoint == 'graphics_cards' && this.selectedGraphicsCard.id && this.recommendedBuild && this.recommendedBuild.id) {
        return true
      }
      if (this.selectedPart.endpoint == 'drives' && this.selectedDrive.id && this.recommendedBuild && this.recommendedBuild.id) {
        return true
      }
      if (this.selectedPart.endpoint == 'motherboards' && this.selectedMotherboard.id && this.recommendedBuild && this.recommendedBuild.id) {
        return true
      }
      if (this.selectedPart.endpoint == 'random_access_memory' && this.selectedRandomAccessMemory.id && this.recommendedBuild && this.recommendedBuild.id) {
        return true
      }
      if (this.selectedPart.endpoint == 'power_supplies' && this.selectedPowerSupply.id && this.recommendedBuild && this.recommendedBuild.id) {
        return true
      }
      return false
    }
   }
}
</script>
