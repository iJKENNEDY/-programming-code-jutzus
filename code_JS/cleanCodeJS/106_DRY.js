import { format } from "path";

const reportData = {
	name: "Software Crafters",
	createdAt: new Date(),
	purchases: 100,
	conversionRate: 20,
}

function withDRY(){
	function formatReport(reportData){
		return `
		Name: ${reportData.name}
		Created at: ${reportData.createdAt}
		Purchases: ${reportData.purchases}
		Conversion Rate: ${reportData.conversionRate}%
		`
	}

	function showReport(reportData) {
		console.log("showing report...", formatReport(reportData));
	}

	function saveReport(reportData) {
		console.log("Saving report...", format(reportData));
	}

	showReport(reportData);
	saveReport(reportData)
}