
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
	entry: './src/index.js', //punto de entrada
	output:{
	path: path.resolve(__dirname, 'dist'),
	filename: 'bundle.js'
},//a√ade punto de salida
resolve: {
	extensions: ['*','.mjs','.js','.svelte'],
}, //a√ade soporte para las extensiones
	module:{
	rules:[
		{
		test: /\.js?$/,
		exclude: /node_modules/,
		use: {
			loader: 'babel-loader',
		},
		}, // creamos la regla para nuestros achivos JS
		{
			test: /\.svelte$/,
			exclude: /node_modules/,
			use: {
				loader: 'svelte-loader'
			}
		
		},//utilizamos svelte-loader para trabajar con los archivos .svelte
	]
},
	plugins:[
		new HtmlWebpackPlugin({
			inject: true,
			template: './public/index.html',
			filename: './index.html',
		})
	]//utilizamos este plugin para a√adir el recurso compilado al documento HTML
};
