<template>
  <div class="w3-row w3-margin-right">
    <div class="w3-row">
      <div class="w3-card-1">
        <div class="w3-container w3-center">
          <img
            v-if="driveData.image_url != 'Placeholder'"
            class="w3-margin-top"
            :src="
              require(`../../assets/products/drive/${driveData.image_url}.jpg`)
            "
            height="100"
          />
          <img
            v-else
            class="w3-margin-top"
            src="../../assets/parts/hard-drive.svg"
            height="100"
          />
          <p>
            <img
              class="w3-margin-top"
              :src="
                require(`../../assets/brand_icons/${driveData.brands.toLowerCase()}.svg`)
              "
              height="15"
            />
          </p>
          <p>
            {{ $t('components.products.drive.description.model') }}:
            {{ driveData.model }}
          </p>
          <p v-if="!short">
            {{ $t('components.products.drive.description.series') }}:
            {{ driveData.drive_series }}
          </p>
          <p v-if="!short">
            {{ $t('components.products.drive.description.formFactor') }}:
            {{ driveData.drive_form_factors }}
          </p>
          <p v-if="!short">
            {{ $t('components.products.drive.description.capacity') }}:
            {{ driveData.capacity_gb }}
          </p>
          <p v-if="!short">
            {{ $t('components.products.drive.description.readSpeed') }}:
            {{ driveData.max_read_mb_s }}
          </p>
          <p v-if="!short">
            {{ $t('components.products.drive.description.writeSpeed') }}:
            {{ driveData.max_write_mb_s }}
          </p>
        </div>
      </div>
    </div>
    <div class="w3-row">
      <button v-on:click="select" class="w3-button w3-deep-orange w3-block">
        {{ $t('components.products.drive.select') }}
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Drive',
  props: ['drive', 'short', 'id'],
  data () {
    return {
      driveData: {},
      products: []
    }
  },
  async created () {
    if (this.id) {
      await axios
        .get(this.$store.state.api_url + '/parts/drives', {
          params: { id: this.id }
        })
        .then(r => r.data)
        .then(data => {
          this.driveData = data.parts[0]
        })
    } else {
      this.driveData = this.drive
    }
  },
  methods: {
    select () {
      this.$store.dispatch('setSelectedDrive', this.driveData)
      this.$store.dispatch('getCompatabilityIssues')
      this.$store.dispatch('getCalculatedPowerUsage')
    }
  }
}
</script>
