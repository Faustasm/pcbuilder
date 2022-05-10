<template>
  <div class="w3-row w3-margin-right">
    <div class="w3-row">
      <div class="w3-card-1">
        <div class="w3-container w3-center">
          <img
            class="w3-margin-top"
            src="../../assets/builds/pc.svg"
            height="100"
          />
          <p>
            {{ $t('components.builds.build.processorName') }}:
            {{ build.processors }}
          </p>
          <p>
            {{ $t('components.builds.build.graphicsCardName') }}:
            {{ build.graphics_cards }}
          </p>
          <p>
            {{ $t('components.builds.build.motherboardName') }}:
            {{ build.motherboards }}
          </p>
          <p>
            {{ $t('components.builds.build.driveName') }}:
            {{ build.drives }}
          </p>
          <p>
            {{ $t('components.builds.build.powerSupplyName') }}:
            {{ build.power_supplies }}
          </p>
          <p>
            {{ $t('components.builds.build.randomAccessMemoryName') }}:
            {{ build.random_access_memory }}
          </p>
        </div>
      </div>
    </div>
    <div class="w3-row">
      <button v-on:click="select(build)" class="w3-button w3-red w3-block">
        {{ $t('components.builds.build.select') }}
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Build',
  props: ['build'],
  methods: {
    select (build) {
      let cpu_id = build.processor_id
      if (cpu_id) {
        let payload = {
          selectedPart: 'processors',
          filters: { id: cpu_id }
        }
        this.$store.dispatch('loadParts', payload)
      }
      let gpu_id = build.graphics_card_id
      if (gpu_id) {
        let payload = {
          selectedPart: 'graphics_cards',
          filters: { id: gpu_id }
        }
        this.$store.dispatch('loadParts', payload)
      }
      let mb_id = build.motherboard_id
      if (mb_id) {
        let payload = {
          selectedPart: 'motherboards',
          filters: { id: mb_id }
        }
        this.$store.dispatch('loadParts', payload)
      }
      let psu_id = build.power_supply_id
      if (psu_id) {
        let payload = {
          selectedPart: 'power_supplies',
          filters: { id: psu_id }
        }
        this.$store.dispatch('loadParts', payload)
      }
      let ram_id = build.random_access_memory_id
      if (ram_id) {
        let payload = {
          selectedPart: 'random_access_memory',
          filters: { id: ram_id }
        }
        this.$store.dispatch('loadParts', payload)
      }
      let drive_id = build.drive_id
      if (drive_id) {
        let payload = {
          selectedPart: 'drives',
          filters: { id: drive_id }
        }
        this.$store.dispatch('loadParts', payload)
      }
    }
  }
}
</script>
