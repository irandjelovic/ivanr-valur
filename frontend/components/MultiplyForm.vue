<template>
  <v-form v-model="formValid" ref="form" lazy-validation>
    <v-row>
      <v-col cols="12" md="2">
        <v-text-field
          v-model="multiplicand"
          label="Enter multiplicand"
          type="number"
          outlined
          dense
          :rules="[requiredRule]"
          required
          data-test="multiplicand-input"
        ></v-text-field>
      </v-col>
      <v-col cols="12" md="2">
        <v-text-field
          v-model="multiplicator"
          label="Enter multiplicator"
          type="number"
          outlined
          dense
          :rules="[requiredRule]"
          required
          data-test="multiplicator-input"
        ></v-text-field>
      </v-col>
      <v-col cols="12" md="2">
        <v-btn :disabled="!formValid" color="primary" @click="multiplyNumbers" data-test="multiply-btn">Multiply</v-btn>
      </v-col>
    </v-row>
  </v-form>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      multiplicand: null,
      multiplicator: null,
      formValid: false,
      requiredRule: value => !!value || 'This field is required'
    }
  },
  emits: ['multiplied'],
  methods: {
    async multiplyNumbers() {
      if (this.$refs.form.validate()) {
        try {
          const response = await axios.get('http://localhost:8009/api/multiply/', {
            params: {
              multiplicand: this.multiplicand,
              multiplicator: this.multiplicator
            }
          });
          this.$emit('multiplied', response.data.res);
        } catch (error) {
          console.error('API error', error);
        }
      }
    }
  }
}
</script>