<template>
  <div>
    <div class="w3-row">
      <div class="w3-col s12 m12 l2">
        <PartSideBar />
      </div>
      <div class="w3-col s12 m12 l8">
        <p>{{ $t('content.contacts_email') }}</p>
        <p>faustasmail15@gmail.com</p>
        <p>Upwork:</p>
        <p><a href="https://www.upwork.com/freelancers/~01743e006f144cda15">https://www.upwork.com/freelancers/~01743e006f144cda15</a></p>
      </div>
    </div>
  </div>
</template>

<script>
import PartSideBar from '@/components/parts/PartSideBar.vue'
export default {
  name: 'Contacts',
  components: {
    PartSideBar
  }
}
</script>
