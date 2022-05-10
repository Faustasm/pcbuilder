import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    selectedProcessor: {},
    selectedGraphicsCard: {},
    selectedMotherboard: {},
    selectedPowerSupply: {},
    selectedRandomAccessMemory: {},
    selectedDrive: {},
    selectedPart: {},
    partsList: [],
    filters: [],
    selectedFilters: {},
    currentPage: null,
    totalPages: null,
    parts: [],
    builds: [],
    recommendedBuild: [],
    generatedBuild: {}
  },
  mutations: {
    setParts (state, data) {
      state.selectedPart = data.selectedPart
      state.partsList = data.partsList
      state.filters = data.filters
      state.currentPage = data.currentPage
      state.totalPages = data.totalPages
      state.parts = data.parts
    },
    setBuilds (state, data) {
      state.filters = data.filters
      state.currentPage = data.currentPage
      state.totalPages = data.totalPages
      state.builds = data.builds
    },
    setRecommendedBuild (state, data) {
      state.recommendedBuild = data.builds[0]
    },
    setGeneratedBuild (state, data) {
      state.recommendedBuild = data
    },
    setSelectedProcessor (state, processor) {
      state.selectedProcessor = processor
    },
    setSelectedGraphicsCard (state, graphicsCard) {
      state.selectedGraphicsCard = graphicsCard
    },
    setSelectedMotherboard (state, motherboard) {
      state.selectedMotherboard = motherboard
    },
    setSelectedPowerSupply (state, powerSupply) {
      state.selectedPowerSupply = powerSupply
    },
    setSelectedRandomAccessMemory (state, randomAccessMemory) {
      state.selectedRandomAccessMemory = randomAccessMemory
    },
    setSelectedFilters (state, filters) {
      state.selectedFilters = filters
    },
    setSelectedDrive (state, drive) {
      state.selectedDrive = drive
    },
    clearSelectedProcessor (state) {
      state.selectedProcessor = {}
    },
    clearSelectedGraphicsCard (state) {
      state.selectedGraphicsCard = {}
    },
    clearSelectedMotherboard (state) {
      state.selectedMotherboard = {}
    },
    clearSelectedPowerSupply (state) {
      state.selectedPowerSupply = {}
    },
    clearSelectedRandomAccessMemory (state) {
      state.selectedRandomAccessMemory = {}
    },
    clearSelectedDrive (state) {
      state.selectedDrive = {}
    }
  },
  actions: {
    loadParts ({ commit }, payload) {
      commit('setSelectedFilters', payload.filters)
      axios
        .get('http://127.0.0.1:5000/parts/' + payload.selectedPart, {
          params: payload.filters
        })
        .then(r => r.data)
        .then(data => {
          if (payload.filters && payload.filters.id) {
            switch (payload.selectedPart) {
              case 'processors':
                commit('setSelectedProcessor', data.parts[0])
                break
              case 'graphics_cards':
                commit('setSelectedGraphicsCard', data.parts[0])
                break
              case 'motherboards':
                commit('setSelectedMotherboard', data.parts[0])
                break
              case 'power_supplies':
                commit('setSelectedPowerSupply', data.parts[0])
                break
              case 'random_access_memory':
                commit('setSelectedRandomAccessMemory', data.parts[0])
                break
              case 'drives':
                commit('setSelectedDrive', data.parts[0])
                break
              default:
                commit('setSelectedProcessor', data.parts[0])
            }
          } else {
            commit('setParts', data)
          }
        })
    },
    loadRecommendedBuilds ({ commit }, payload) {
      axios
        .get('http://127.0.0.1:5000/builds', {
          params: payload.filters
        })
        .then(r => r.data)
        .then(data => {
          commit('setRecommendedBuild', data)
        })
    },
    loadBuilds ({ commit }, payload) {
      commit('setSelectedFilters', payload.filters)
      axios
        .get('http://127.0.0.1:5000/builds', {
          params: payload.filters
        })
        .then(r => r.data)
        .then(data => {
          commit('setBuilds', data)
        })
    },
    createBuild ({ commit }, payload) {
      axios
        .post('http://127.0.0.1:5000/builds', {
          payload: payload
        })
        .then(r => r.data)
        .then(data => {
          commit('setGeneratedBuild', data)
        })
    },
    setSelectedProcessor ({ commit }, processor) {
      commit('setSelectedProcessor', processor)
    },
    clearSelectedProcessor ({ commit }) {
      commit('clearSelectedProcessor')
    },
    setSelectedGraphicsCard ({ commit }, graphicsCard) {
      commit('setSelectedGraphicsCard', graphicsCard)
    },
    clearSelectedGraphicsCard ({ commit }) {
      commit('clearSelectedGraphicsCard')
    },
    setSelectedMotherboard ({ commit }, motherboard) {
      commit('setSelectedMotherboard', motherboard)
    },
    clearSelectedMotherboard ({ commit }) {
      commit('clearSelectedMotherboard')
    },
    setSelectedPowerSupply ({ commit }, powerSupply) {
      commit('setSelectedPowerSupply', powerSupply)
    },
    clearSelectedPowerSupply ({ commit }) {
      commit('clearSelectedPowerSupply')
    },
    setSelectedRandomAccessMemory ({ commit }, randomAccessMemory) {
      commit('setSelectedRandomAccessMemory', randomAccessMemory)
    },
    clearSelectedRandomAccessMemory ({ commit }) {
      commit('clearSelectedRandomAccessMemory')
    },
    setSelectedFilters ({ commit }, filters) {
      commit('setSelectedFilters', filters)
    },
    setSelectedDrive ({ commit }, drive) {
      commit('setSelectedDrive', drive)
    },
    clearSelectedDrive ({ commit }) {
      commit('clearSelectedDrive')
    }
  }
})
