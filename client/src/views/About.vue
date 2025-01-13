<template>
  <div>
    <div class="w3-row">
      <div class="w3-col s12 m12 l2">
        <PartSideBar />
      </div>
      <div class="w3-col s12 m12 l8">
        <p>{{ $t('content.about_content_description') }}</p>
        <p>{{ $t('content.about_content_tech_stack_header') }}</p>
        <p>{{ $t('content.about_content_tech_stack') }}</p>
        <p>{{ $t('content.about_content_source_code') }}</p>
        <p><a href="https://github.com/Faustasm/pcbuilder">https://github.com/Faustasm/pcbuilder</a></p>
      </div>
    </div>
  </div>
</template>

<script>
import PartSideBar from '@/components/parts/PartSideBar.vue'
export default {
  name: 'About',
  components: {
    PartSideBar
  }
}
</script>
