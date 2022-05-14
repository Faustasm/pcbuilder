<template>
  <div class="w3-container">
    <div class="w3-panel w3-round-xlarge w3-green" v-if="showOkMessage">
      <h2>
        {{ $t('components.parts.partSideBar.okHeader') }}
      </h2>
      <p>
        {{ $t('components.parts.partSideBar.okMessage') }}
      </p>
    </div>
    <div
      class="w3-panel w3-round-xlarge w3-red"
      v-for="compatabilityIssue in compatabilityIssues"
      :key="compatabilityIssue"
    >
      <h2>
        {{ $t('components.parts.partSideBar.attentionHeader') }}
      </h2>
      <p>
        {{ $t(`components.parts.partSideBar.${compatabilityIssue}`) }}
      </p>
    </div>
    <div class="w3-panel w3-round-xlarge w3-light-grey">
      <div class="w3-row">
        <div class="w3-left">
          <img
            class="w3-margin"
            src="../../assets/parts/supply.svg"
            height="30"
          />
        </div>
        <div class="w3-right">
          <div class="w3-row">
            <div class="w3-left">
              <p class="w3-margin" v-if="selectedPowerSupply.max_power_w">
                {{ requiredPower }}/{{ selectedPowerSupply.max_power_w }}
              </p>
              <p class="w3-margin" v-else>
                Nepasirinkta
              </p>
            </div>
            <div class="w3-right">
              <img
                class="w3-margin"
                src="../../assets/lighting.svg"
                height="30"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="w3-button w3-round-xlarge w3-block w3-orange"
      v-if="showPsuCalculations"
      @click="generateUrl"
    >
      {{ $t('components.parts.partSideBar.generateUrl') }}
    </div>
    <div class="w3-margin-top">
      <Processor />
      <GraphicsCard />
      <Motherboard />
      <PowerSupply />
      <RandomAccessMemory />
      <Drive />
    </div>
  </div>
</template>

<script>
import store from '../../store'
import Processor from '@/components/parts/Processor'
import GraphicsCard from '@/components/parts/GraphicsCard'
import Motherboard from '@/components/parts/Motherboard'
import RandomAccessMemory from '@/components/parts/RandomAccessMemory'
import PowerSupply from '@/components/parts/PowerSupply'
import Drive from '@/components/parts/Drive'
export default {
  name: 'PartSideBar',
  components: {
    Processor,
    GraphicsCard,
    Motherboard,
    RandomAccessMemory,
    PowerSupply,
    Drive
  },
  data () {
    return {
      cpu: '',
      gpu: '',
      mb: '',
      psu: '',
      ram: '',
      drive: ''
    }
  },
  mounted () {
    let cpu_id = this.$route.query.cpu
    if (cpu_id) {
      this.cpu = this.$route.query.cpu
      let payload = {
        selectedPart: 'processors',
        filters: { id: cpu_id }
      }
      this.$store.dispatch('loadParts', payload)
    }
    let gpu_id = this.$route.query.gpu
    if (gpu_id) {
      this.gpu = this.$route.query.gpu
      let payload = {
        selectedPart: 'graphics_cards',
        filters: { id: gpu_id }
      }
      this.$store.dispatch('loadParts', payload)
    }
    let mb_id = this.$route.query.mb
    if (mb_id) {
      this.mb = this.$route.query.mb
      let payload = {
        selectedPart: 'motherboards',
        filters: { id: mb_id }
      }
      this.$store.dispatch('loadParts', payload)
    }
    let psu_id = this.$route.query.psu
    if (psu_id) {
      this.psu = this.$route.query.psu
      let payload = {
        selectedPart: 'power_supplies',
        filters: { id: psu_id }
      }
      this.$store.dispatch('loadParts', payload)
    }
    let ram_id = this.$route.query.ram
    if (ram_id) {
      this.ram = this.$route.query.ram
      let payload = {
        selectedPart: 'random_access_memory',
        filters: { id: ram_id }
      }
      this.$store.dispatch('loadParts', payload)
    }
    let drive_id = this.$route.query.drive
    if (drive_id) {
      this.drive = this.$route.query.drive
      let payload = {
        selectedPart: 'drives',
        filters: { id: drive_id }
      }
      this.$store.dispatch('loadParts', payload)
    }
  },
  methods: {
    generateUrl () {
      let baseUrl = 'http://localhost:8080?'
      if (this.selectedProcessor && this.selectedProcessor.id) {
        baseUrl += `cpu=${this.selectedProcessor.id}`
      }
      if (this.selectedGraphicsCard && this.selectedGraphicsCard.id) {
        baseUrl += `&gpu=${this.selectedGraphicsCard.id}`
      }
      if (this.selectedMotherboard && this.selectedMotherboard.id) {
        baseUrl += `&mb=${this.selectedMotherboard.id}`
      }
      if (
        this.selectedRandomAccessMemory &&
        this.selectedRandomAccessMemory.id
      ) {
        baseUrl += `&ram=${this.selectedRandomAccessMemory.id}`
      }
      if (this.selectedDrive && this.selectedDrive.id) {
        baseUrl += `&drive=${this.selectedDrive.id}`
      }
      if (this.selectedPowerSupply && this.selectedPowerSupply.id) {
        baseUrl += `&psu=${this.selectedPowerSupply.id}`
      }
      let payload = {
        processor_id: this.selectedProcessor.id,
        graphics_card_id: this.selectedGraphicsCard.id,
        motherboard_id: this.selectedMotherboard.id,
        drive_id: this.selectedDrive.id,
        random_access_memory_id: this.selectedRandomAccessMemory.id,
        power_supply_id: this.selectedPowerSupply.id
      }
      this.$store.dispatch('createBuild', payload)
      navigator.clipboard.writeText(baseUrl)
      alert('Nuoroda nukopijuota')
      this.$store.dispatch('loadBuilds')
    }
  },
  computed: {
    compatabilityIssues: () => store.state.compatabilityIssues,
    requiredPower: () => store.state.requiredPower,
    selectedProcessor: () => store.state.selectedProcessor,
    selectedGraphicsCard: () => store.state.selectedGraphicsCard,
    selectedMotherboard: () => store.state.selectedMotherboard,
    selectedRandomAccessMemory: () => store.state.selectedRandomAccessMemory,
    selectedPowerSupply: () => store.state.selectedPowerSupply,
    selectedDrive: () => store.state.selectedDrive,
    showOkMessage: function () {
      return this.compatabilityIssues && this.compatabilityIssues.length === 0
    },
    showPsuCalculations: function () {
      return (
        this.selectedProcessor.id ||
        this.selectedGraphicsCard.id ||
        this.selectedMotherboard.id ||
        this.selectedRandomAccessMemory.id ||
        this.selectedPowerSupply.id ||
        this.selectedDrive.id
      )
    }
  }
}
</script>
