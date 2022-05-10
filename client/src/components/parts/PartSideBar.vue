<template>
  <div class="w3-container">
    <div class="w3-panel w3-bottombar">
      <div class="w3-row w3-center" v-if="showPsuCalculations">
          <div class="w3-quarter">
            <img class="w3-margin-top" src="../../assets/parts/supply.svg" height="30">
          </div>
          <div class="w3-threequarter">
            <div class="w3-third">
              <p>{{requiredPower}}/{{selectedPowerSupply.max_power_w}}</p>
            </div>
            <div class="w3-twothird">
              <img class="w3-margin-top" src="../../assets/lighting.svg" height="30">
            </div>
          </div>
      </div>
    </div>
    <div class="w3-panel w3-green" v-if="showOkMessage">
      <img
         class="w3-margin-top"
         src="../../assets/thumbs_up.svg"
         height="50"
     />
      <p>Suderinamumo problemų nerasta.</p>
  </div>
    <div class="w3-panel w3-red" v-if="showCpuSocketeMissmatchMessage">
      <h2>Dėmesio!</h2>
      <p>Procesoriaus jungtis nesutampa su motininės plokštės jungtimi.</p>
    </div>
    <div class="w3-panel w3-red" v-if="showCpuRandomAccessMemoryMismatchMessage">
      <h2>Dėmesio!</h2>
      <p>Procesoriaus nepalaiko šio atminties tipo.</p>
    </div>
    <div class="w3-panel w3-red" v-if="showCpuRandomAccessMemoryCapacityMessage">
      <h2>Dėmesio!</h2>
      <p>Procesoriaus nepalaiko tiek atminties.</p>
    </div>
    <div class="w3-panel w3-red" v-if="showMbRandomAccessMemoryMismatchMessage">
      <h2>Dėmesio!</h2>
      <p>Motininė plokštė nepalaiko šio atminties tipo.</p>
    </div>
    <div class="w3-panel w3-red" v-if="showMbRandomAccessMemoryCapacityMessage">
      <h2>Dėmesio!</h2>
      <p>Motininė plokštė nepalaiko tiek atminties.</p>
    </div>
    <div class="w3-panel w3-yellow" v-if="showRamDualChannelWarningMessage">
      <h3>Perspėjimas!</h3>
      <p>Rekomenduojama naudoti operatyvia atmintį iš dviejų modulių, kad atmintis veiktu dviejų kanalų režimu.</p>
    </div>
    <div class="w3-button w3-block w3-orange" v-if="showOkMessage && showPsuCalculations" @click="generateUrl">
      Generuoti nuorodą
    </div>
    <div class="w3-margin-top">
      <Processor/>
      <GraphicsCard/>
      <Motherboard/>
      <PowerSupply/>
      <RandomAccessMemory/>
      <Drive/>
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
  data() {
    return {
      cpu: "",
      gpu: "",
      mb: "",
      psu: "",
      ram: "",
      drive: ""
    }
  },
  mounted () {
    let cpu_id = this.$route.query.cpu
    if (cpu_id) {
      this.cpu = this.$route.query.cpu
      let payload = {
        'selectedPart': 'processors',
        'filters': {'id': cpu_id}
      }
      this.$store.dispatch('loadParts', payload)
    }
    let gpu_id = this.$route.query.gpu
    if (gpu_id) {
      this.gpu = this.$route.query.gpu
      let payload = {
        'selectedPart': 'graphics_cards',
        'filters': {'id': gpu_id}
      }
      this.$store.dispatch('loadParts', payload)
    }
    let mb_id = this.$route.query.mb
    if (mb_id) {
      this.mb = this.$route.query.mb
      let payload = {
        'selectedPart': 'motherboards',
        'filters': {'id': mb_id}
      }
      this.$store.dispatch('loadParts', payload)
    }
    let psu_id = this.$route.query.psu
    if (psu_id) {
      this.psu = this.$route.query.psu
      let payload = {
        'selectedPart': 'power_supplies',
        'filters': {'id': psu_id}
      }
      this.$store.dispatch('loadParts', payload)
    }
    let ram_id = this.$route.query.ram
    if (ram_id) {
      this.ram = this.$route.query.ram
      let payload = {
        'selectedPart': 'random_access_memory',
        'filters': {'id': ram_id}
      }
      this.$store.dispatch('loadParts', payload)
    }
    let drive_id = this.$route.query.drive
    if (drive_id) {
      this.drive = this.$route.query.drive
      let payload = {
        'selectedPart': 'drives',
        'filters': {'id': drive_id}
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
      if (this.selectedRandomAccessMemory && this.selectedRandomAccessMemory.id) {
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
    selectedProcessor: () => store.state.selectedProcessor,
    selectedGraphicsCard: () => store.state.selectedGraphicsCard,
    selectedMotherboard: () => store.state.selectedMotherboard,
    selectedRandomAccessMemory: () => store.state.selectedRandomAccessMemory,
    selectedPowerSupply: () => store.state.selectedPowerSupply,
    selectedDrive: () => store.state.selectedDrive,
    showCpuSocketeMissmatchMessage: function() {
      if (this.selectedProcessor.sockets && this.selectedMotherboard.sockets) {
        return this.selectedProcessor.sockets !== this.selectedMotherboard.sockets
      } else {
        return false
      }
    },
    showCpuRandomAccessMemoryMismatchMessage: function() {
      if (this.selectedProcessor.ram_memory_types && this.selectedRandomAccessMemory.ram_memory_types) {
        return this.selectedProcessor.ram_memory_types !== this.selectedRandomAccessMemory.ram_memory_types
      } else {
        return false
      }
    },
    showCpuRandomAccessMemoryCapacityMessage: function() {
      if (this.selectedProcessor.max_memory_supported && this.selectedRandomAccessMemory.total_capacity_gb) {
        return this.selectedProcessor.max_memory_supported < this.selectedRandomAccessMemory.total_capacity_gb
      } else {
        return false
      }
    },
    showMbRandomAccessMemoryMismatchMessage: function () {
      if (this.selectedMotherboard.ram_memory_types && this.selectedRandomAccessMemory.ram_memory_types) {
        return this.selectedMotherboard.ram_memory_types !== this.selectedRandomAccessMemory.ram_memory_types
      } else {
        return false
      }
    },
    showMbRandomAccessMemoryCapacityMessage: function () {
      if (this.selectedMotherboard.ram_memory_types && this.selectedRandomAccessMemory.ram_memory_types) {
        return this.selectedMotherboard.max_memory_supported < this.selectedRandomAccessMemory.total_capacity_gb
      } else {
        return false
      }
    },
    showRamDualChannelWarningMessage: function () {
      return this.selectedRandomAccessMemory.modules === 1
    },
    showOkMessage: function () {
      return !this.showCpuSocketeMissmatchMessage &&
      !this.showCpuRandomAccessMemoryMismatchMessage &&
      !this.showCpuRandomAccessMemoryCapacityMessage &&
      !this.showMbRandomAccessMemoryMismatchMessage &&
      !this.showMbRandomAccessMemoryCapacityMessage &&
      !this.showRamDualChannelWarningMessage
    },
    showPsuCalculations: function () {
      return this.selectedPowerSupply.max_power_w
    },
    requiredPower: function () {
      return (this.selectedProcessor.thermal_design_power_w || 0) +
      (this.selectedGraphicsCard.thermal_design_power_w || 0) +
      (this.selectedMotherboard.model ? 150 : 0) +
      (this.selectedRandomAccessMemory.modules ? this.selectedRandomAccessMemory.modules * 15 : 0) +
      (this.selectedDrive.model ? 30 : 0)
    }
  }
}
</script>
