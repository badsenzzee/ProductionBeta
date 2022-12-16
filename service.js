/// <reference types="Cypress" />

//get credentials users(Dianita)
Cypress.Commands.add('getTokenService', (username, password) => {
 const url = `https://prod.systems.greenanimals.com/systemsconsensus/api/security/loginconsensus`
 cy.request({
 method: 'POST',
 url: url,
 form: true,
 headers: {
 "Connection": "keep-alive",
 'ipaddress': '169.253.169.253',
 'Content-Type': 'application/json; charset=utf-8',
 'BrowserDevice': 'Chrome'
 },
 body: {
 "grant_type": "password",
 "client_id": "8a3e4d10a9a92e7b9c55c88a73abc123",
 "username": username,
 "password": password
 }
 }).then(function (response) {
 expect(response.status).to.eq(200);
 expect(response.body.user_data).to.include(username.toUpperCase().toString());
 window.localStorage.setItem("tokenType", response.body.token_type);
 window.localStorage.setItem("accessToken", response.body.access_token);
 })
});

//get dates contract 
Cypress.Commands.add('filterForAuthorizationService', (numContract) => {
 const url = `https://prod.systems.greenanimals.com/systemsconsensus/api/contract/filterFortransaction`
 cy.request({
 method: 'POST',
 url: url,
 form: true,
 headers: {
 "Connection": "keep-alive",
 'Accept': 'application/json',
 'Accept-Encoding': 'gzip, deflate, br',
 'Authorization': window.localStorage.getItem("tokenType") + " " + window.localStorage.getItem("accessToken"),
 'Host': 'prod.systems.greenanimals.com',
 'Origin': 'https://prod.greenanimals.com',
 'Referer': 'https://prod.greenanimals.com/',
 'Content-Type': 'application/json; charset=utf-8',
 },
 body: {
 "numberscontract": numContract,
 "filterByAuthorization": false,
 "filterByBusiness": false,
 "filterBySettlement": false,
 "filterBynumbersOn": false,
 "filterConditioncontract": false
 }
 }).then(function (response) {
 expect(response.status).to.eq(200);
 expect(response.body.data[0].numberscontract).to.eq(parseInt(numContract));
 return cy.wrap(response.body);
 })
});

//get late payments 
Cypress.Commands.add('getDefaulterDetailsService', (numContract) => {
 cy.filterForAuthorizationService(numContract).then(value => {
 const url = `https://prod.systems.greenanimals.com/systemsconsensus/api/quotation/GetDetailsMora/`
 + value.data[0].CodeRegion + '/' + value.data[0].CodeProduct + '/' + value.data[0].numberscontract
 cy.request({
 method: 'GET',
 url: url,
 headers: {
 'ApplicationCode': 28,
 'CodePlatform': 7,
 'Authorization': window.localStorage.getItem("tokenType") + " " + window.localStorage.getItem("accessToken"),
 'ipaddress': '169.253.169.253',
 'BrowserDevice': 'Chrome',
 'OperatingSystem': 'Windows',
 'Content-Type': 'application/json; charset=utf-8'
 }
 }).then(function (response) {
 expect(response.status).to.eq(200);
 return cy.wrap(response.body);
 })
 });
});

Cypress.Commands.add('getDeductibleInformationService', (numContract) => {
 cy.filterForAuthorizationService(numContract).then(value => {
 const url = `http://prod.systems.greenanimals.com/systemscontract/api/contract/GetcontractPerDocument?typedocument=C&numbersdocument=`
 +value.data[0].idCard +'&filterCorporateOld=+false'
 cy.request({
 method: 'GET',
 url: url,
 headers: {
 'Accept': 'application/json',
 'ApplicationCode': 28,
 'CodePlatform': 7,
 'Authorization': window.localStorage.getItem("tokenType") + " " + window.localStorage.getItem("accessToken"),
 'ipaddress': '169.253.169.253',
 'BrowserDevice': 'Chrome',
 'OperatingSystem': 'Windows',
 'Content-Type': 'application/json; charset=utf-8'
 }
 }).then(function (response) {
 expect(response.status).to.eq(200);
 return cy.wrap(response.body);
 })
 });
});
