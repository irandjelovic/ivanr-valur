<template>
  <v-app>
    <v-container class="pa-4">
        <multiply-form @multiplied="(res) => result = res" />
        <v-row>
          <v-col cols="12" md="4">
            <v-alert v-show="result !== null" type="info" class="mt-4">Result: <span data-test="result-info">{{ result }}</span></v-alert>
          </v-col>
        </v-row>
    </v-container>
  </v-app>
</template>

<script>
import MultiplyForm from '../components/MultiplyForm.vue';

export default {
  components: {
    MultiplyForm
  },
  data() {
    return {
      result: null
    }
  }
}
</script>