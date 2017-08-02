const regex = /<\//g;
const str = `<!DOCTYPE html>
<html >

<head>
  <meta charset="UTF-8">
  <title>GCard</title>
  
  
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="/static/css/font.min.css">
  <link rel="stylesheet" href="/static/css/font.css ">
  <link rel="stylesheet" href="/static/css/index.css">
  <style>

  #czz {
	width: 300px;
  height: 300px;}
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #a9a9a9;
    height: 60px;
    margin-top: 10px;
    border-radius: 4px;
}

li {
    float: left;
}

li a {
    display: block;
    color: white;
    text-align: center;
    padding: 22px 16px;
    text-decoration: none;
}

/* Change the link color to #111 (black) on hover */
li a:hover {
    background-color: gray;
}
.active {
    background-color: #4CAF50;
    color: white;
}
  .header {
    width: 81%;
    height: 86px;
    border-radius: 8px;
    margin-left: auto;
    margin-right: auto;
  }
   
button{
    background-color: #4CAF50;
    border: none;
    width: 50%;
    color: white;
    padding: 16px 32px;
    text-decoration: none;
    margin: 4px 2px;
    cursor: pointer;
    transition: width 0.4s ease-in-out;
    -webkit-transition: width 0.4s ease-in-out;

}
input {
    width: 50%;
    box-sizing: border-box;
    border: 2px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
    background-color: white;
    background-image: url('https://cdn0.iconfinder.com/data/icons/octicons/1024/credit-card-16.png');
    background-position: 10px 10px; 
    background-repeat: no-repeat;
    padding: 12px 20px 12px 40px;
    -webkit-transition: width 0.4s ease-in-out;
    transition: width 0.4s ease-in-out;
}
</style>
</head>
    <div class="header">
        <ul class="liste">
            <li><a href="/" class="active"><i class="fa fa-home">  Home</i></a></li>
            
            <li><a href="/accounts/login/"><i class="fa fa-key"> Login</i></a></li>
            <li><a href="/signup"><i class="fa fa-address-card">Register</i></a></li>
            
            <li><a href="# "><i class="fa fa-profile">'s Account</i></a></li>
        </ul>
    </div>
<body translate="no" onload="myFunction()" >
    <div class="wrapper">
	<div class="desc">
		<h1>GCARD ~ EW2C</h1>
		<p>Express Way To E-Commerce Without Sharing Any CC Info / Mobile Info</p>
	</div>
	<div class="content">
		<!-- content here -->
        <center>
		<div class="product-grid product-grid--flexbox">
			<div class="product-grid__wrapper">
				<form action="" method="POST">
				
                <input type='hidden' name='csrfmiddlewaretoken' value='W2kZ3wwp69WkC3X1Gp9mLsLJ5QMp3CPEHkq6Cy2qltOhF4Brh38yPXMNqXfmHXZr' />
				<p><label for="id_username">Username:</label> <input type="text" name="username" maxlength="150" autofocus required id="id_username" /> <span class="helptext">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span></p>
<p><label for="id_password1">Password:</label> <input type="password" name="password1" required id="id_password1" /> <span class="helptext"><ul><li>Your password can&#39;t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can&#39;t be a commonly used password.</li><li>Your password can&#39;t be entirely numeric.</li></ul></span></p>
<p><label for="id_password2">Password confirmation:</label> <input type="password" name="password2" required id="id_password2" /> <span class="helptext">Enter the same password as before, for verification.</span></p>
				<button type="submit">Save</button>
                </form></div></div>
            </center>
            </body>
  <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <script>
    </script>
</body>
</html>	
`;
let m;

while ((m = regex.exec(str)) !== null) {
    // This is necessary to avoid infinite loops with zero-width matches
    if (m.index === regex.lastIndex) {
        regex.lastIndex++;
    }
    
    // The result can be accessed through the `m`-variable.
    m.forEach((match, groupIndex) => {
        console.log(`Found match, group ${groupIndex}: ${match}`);
    });
}
