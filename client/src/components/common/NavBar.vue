<template>
  <div class="w3-row">
    <div class="w3-col s12 m2 l2 w3-center w3-win8-orange" style="height:130px">
      <img
        class="w3-margin-top"
        src="../../assets/navbar_icons/pc-tower.svg"
        height="50"
      />
      <h2 class="w3-text-black">
        {{ $t('components.common.navBar.domainName') }}
      </h2>
    </div>
    <router-link to="/">
      <div
        class="w3-col s12 m2 l2 w3-center w3-black"
        style="height:130px"
        @click="setActiveTab(0)"
        @mouseenter="addClass"
        @mouseleave="removeClass"
      >
        <img
          class="w3-margin-top"
          src="../../assets/navbar_icons/tools.svg"
          height="50"
        />
        <p class="w3-text-white">
          {{ $t('components.common.navBar.home') }}
        </p>
      </div>
    </router-link>
    <router-link to="/recommendation-system">
      <div
        class="w3-col s12 m2 l2 w3-center w3-black"
        style="height:130px"
        @click="setActiveTab(1)"
        @mouseenter="addClass"
        @mouseleave="removeClass"
      >
        <img
          class="w3-margin-top"
          src="../../assets/navbar_icons/rec.svg"
          height="50"
        />
        <p class="w3-text-white">
          {{ $t('components.common.navBar.recommendationSystem') }}
        </p>
      </div>
    </router-link>
    <router-link to="/api">
      <div
        class="w3-col s12 m2 l2 w3-center w3-black"
        style="height:130px"
        @click="setActiveTab(2)"
        @mouseenter="addClass"
        @mouseleave="removeClass"
      >
        <img
          class="w3-margin-top"
          src="../../assets/navbar_icons/api.svg"
          height="50"
        />
        <p class="w3-text-white">
          {{ $t('components.common.navBar.api') }}
        </p>
      </div>
    </router-link>
    <router-link to="/about">
      <div
        class="w3-col s12 m2 l2 w3-center w3-black"
        style="height:130px"
        @click="setActiveTab(3)"
        @mouseenter="addClass"
        @mouseleave="removeClass"
      >
        <img
          class="w3-margin-top"
          src="../../assets/navbar_icons/information.svg"
          height="50"
        />
        <p class="w3-text-white">
          {{ $t('components.common.navBar.about') }}
        </p>
      </div>
    </router-link>
    <router-link to="/contacts">
      <div
        class="w3-col s12 m2 l2 w3-center w3-black"
        style="height:130px"
        @click="setActiveTab(4)"
        @mouseenter="addClass"
        @mouseleave="removeClass"
      >
        <img
          class="w3-margin-top"
          src="../../assets/navbar_icons/mail.svg"
          height="50"
        />
        <p class="w3-text-white">
          {{ $t('components.common.navBar.contacts') }}
        </p>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  data () {
    return {
      activeTab: 0
    }
  },
  methods: {
    addClass: function (e) {
      e.target.classList.remove('w3-black')
      e.target.classList.add('w3-win8-orange')
    },
    removeClass: function (e) {
      e.target.classList.remove('w3-win8-orange')
      e.target.classList.add('w3-black')
    },
    setActiveTab: function (tab) {
      this.activeTab = tab
    }
  }
}
</script>

<style>
.w3-win8-orange {
  color: #fff;
  background-color: #fa6800;
}
</style>
