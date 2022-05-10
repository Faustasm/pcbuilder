<template>
  <div class="w3-margin-top">
    <div class="w3-row">
      <div class="w3-col s12 m12 l12">
        <Paginator/>
      </div>
    </div>
    <div class="w3-container w3-margin-top">
      <div class="w3-row">
          <div
            class="w3-col s12 m12 l4"
            v-for="build in builds"
            :key="build.id"
          >
          <Build
            :build="build"
          />
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import store from '../../store'
import Paginator from '@/components/common/Paginator'
import Build from '@/components/builds/Build'
export default {
  name: 'BuildTable',
  components: {Paginator, Build},
  computed: {
     builds: () => store.state.builds
   }
}
</script>
