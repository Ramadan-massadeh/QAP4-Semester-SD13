/*The St. John’s Marina & Yacht Club is tired of all the paper
it keeps tracking who has their yachts docked at the club,
how much to charge them each month, and if the
members have paid their bill. They decided the need to
start with a program to allow them to enter the
appropriate information and prepare a receipt.

Auther : Ramadan Masadekh
Date : Nov 24 , 2024 */



// Constant

const TOTAL_SITES = 100; 
const EVEN_SITES = 80.00;
const ODD_SITES=120.00;
const ALTERNATE_COST=5.00;
const CLEANING_CHARGE = 50.00;
const VIDEO_SIRV=35.00;
const HST_RATE =.15;
const STANDERED_MEM = 75.00;
const EXE_MEMBER=150.00;
const PROCECING_FEE=59.99;
const CANCEL_FEE=.60;



// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
    style: "currency",
    currency: "CAD",
    minimumFractionDigits: "2",
    maximumFractionDigits: "2",
  });
  
  const per2Format = new Intl.NumberFormat("en-CA", {
    style: "percent",
    minimumFractionDigits: "2",
    maximumFractionDigits: "2",
  });
  
  const per0Format = new Intl.NumberFormat("en-CA", {
    style: "percent",
    minimumFractionDigits: "0",
    maximumFractionDigits: "0",
  });
  
  const com2Format = new Intl.NumberFormat("en-CA", {
    style: "decimal",
    minimumFractionDigits: "2",
    maximumFractionDigits: "2",
  });



// Input User ##

let CurDate= prompt("Enter the date (YYYY-MM-DD): ");
CurDate = new Date(CurDate);
let CurDateStr = CurDate.toDateString();
console.log(CurDateStr.slice(3));


const siteNumber = parseInt(prompt("Enter the site number (1-100):"));
if (siteNumber < 1 || siteNumber > 100) {
    console.error("Invalid site number. Must be between 1 and 100.");
}


let Fname = prompt ("Enter the first name: ");
Fname = Fname.charAt(0).toUpperCase() + Fname.slice(1).toLowerCase();

let Lname = prompt("Enter the last name: ");
Lname = Lname.charAt(0).toUpperCase() + Lname.slice(1).toLowerCase();
let FullName = Fname +" "+ Lname;

console.log(FullName);

let StAdress = prompt("Enter the street address: ");
StAdress=StAdress.charAt(0).toUpperCase() + StAdress.slice(1).toLocaleLowerCase();

let City = prompt("Enter the City: ");
City=City.charAt(0).toUpperCase() + City.slice(1).toLowerCase();

let Province = prompt("Enter the Province: ");
Province=Province.toLocaleUpperCase();

let PoCode=prompt("Enter the Postal Code: ");
PoCode=PoCode.toLocaleUpperCase();

let FullAdd = StAdress + "\n" +City +","+" " +Province +" " + PoCode;

console.log(FullAdd);


let PhoneNumber = prompt ("Enter the Phone number (XXX-XXXX-XXX): ")
let CellNumber = prompt ("Enter the Cell number (XXX-XXXX-XXX): ")
let MemershipType = prompt ("Enter the member ship type (S for Standard, E for Executive): ");
MemershipType = MemershipType.toLocaleUpperCase();

let AlternatMember = prompt ("Enter the the number of alternate members : ");
AlternatMember = parseInt(AlternatMember);

let WeeklySiteCleaning = prompt ("Enter the the weekly site cleaning (Y for Yes, N for No) : ");
WeeklySiteCleaning = WeeklySiteCleaning.toLocaleUpperCase();
let VideoSurv = prompt ("video surveillance (Y for Yes, N for No): ");
VideoSurv = VideoSurv.toLocaleUpperCase();



 // Calculations program ##
//  Determine the site charge based on site number
let SiteCost = 0; 
    if (siteNumber %2==0){
        SiteCost=EVEN_SITES;

    }
    else {
        SiteCost=ODD_SITES;
    }
 console.log("Sitecost is = " + SiteCost);

// Calculate the alternate member charge
let AlternateMembersChargs = parseFloat(AlternatMember * ALTERNATE_COST);

// Add these two numbers to get the site charges.
let Total_Site_Charge=parseFloat(AlternateMembersChargs + SiteCost);
 

 let ExtraChar = 0;
 let Cleaining=0;
 let Vid=0;
// weekly site cleaning
 if (WeeklySiteCleaning == 'Y'){
    Cleaining = CLEANING_CHARGE;
    WeeklySiteCleaning="YES";
 }
 else {
    WeeklySiteCleaning="NO";

 }
 // video surveillance
 if (VideoSurv == 'Y'){
    Vid = VIDEO_SIRV;
    VideoSurv = "YES"
 }
 else {
    VideoSurv="NO";

 }
 // Add these together to determine the extra charges.
ExtraChar = parseFloat(Cleaining + Vid);

console.log("ExtraChar is = " + ExtraChar);

// The subtotal is the site charge plus the extra charges.

let SubTotal = parseFloat(Total_Site_Charge + ExtraChar);

console.log("SubTotal is = " + SubTotal);

// Taxes are calculated at 15% on subtotal

let Hst = parseFloat( SubTotal * HST_RATE);

// The total monthly charge is the subtotal plus the taxes.

let TotalMonthly = parseFloat(SubTotal + Hst);


// Finally monthly dues are calculated at $75.00 for standard 
// members and $150.00 for executive members.

let MonthlyDues = 0;
if (MemershipType == 'S'){
    MonthlyDues = parseFloat(STANDERED_MEM);
    MemershipType='Standard'

}
else{
    MonthlyDues = parseFloat (EXE_MEMBER);
    MemershipType='Executive'

}

console.log("MonthlyDues = " + MonthlyDues);

// The total monthly charge and the monthly dues are added
// together to give the Total Monthly Fees.

let TotalMonthlyFees = parseFloat(TotalMonthly + MonthlyDues);

console.log("TotalMonthlyFees = " + TotalMonthlyFees);


//  determine the total Yearly Fees by multiplying the total monthly fees by 12.

let TotalYearly = parseFloat(TotalMonthly * 12);

// The monthly payment is the
// Total yearly fees, plus a processing fee of $59.99 divided by 12.

let MonthlyPayment = parseFloat((TotalYearly + PROCECING_FEE ) / 12);

//  a cancellation fee, if the client leaves 
// the marina without proper notice, as 60% of the yearly site charges.

// Calculate cancellation fee
let TotalYearCharge = parseFloat(Total_Site_Charge  * 12);
let cancellationFee = parseFloat(TotalYearCharge * CANCEL_FEE);


// Generate randome number for Hse Reg No

function generateRandomNumber() {
    // Generate random numbers for each section
    const part1 = Math.floor(100 + Math.random() * 900); // 3 digits
    const part2 = Math.floor(10 + Math.random() * 90);   // 2 digits
    const part3 = Math.floor(1000 + Math.random() * 9000); // 4 digits
    const part4 = Math.floor(10 + Math.random() * 90);   // 2 digits

    // Combine parts with dashes
    const randomNumber = `${part1}-${part2}-${part3}-${part4}`;
    return randomNumber;
}

const randomFormattedNumber = generateRandomNumber();


// Generate the sales receipt.

document.write("<table class ='resultstable'>");

document.write("<tr>");
document.write(
    "<td class='centertext' colspan='2'><br />St. John’s Marina & Yacht Club<br />Yearly Member Receipt<br /> <br /></td>"
  );
  document.write("</tr>");
  document.write("<tr>");
document.write(
    "<td class = 'lefttext colspan = '2'> <br /> Client Name and Address: <br /><br /> <hr> "+ 
    FullName + "<br /> <br />" + 
    FullAdd+"<br /><br />" + "Phone: "+ PhoneNumber +" (H) <br />   <span class='white'>Phone:</span>    "+
    +CellNumber+" (C) <br /> <br />" +"</td>" 
);
document.write("</tr>");

document.write("<tr>");

document.write("<td class='lefttext' colspan = '2' <br /> Site #:" + siteNumber +
     "<span class='white'>#######################</span>" + "<span class='righttext'>Member type:</span> " + 
     MemershipType +"<br />" +"</td>"
);
document.write("</tr>");


document.write("<tr>");

document.write("<td class='lefttext' colspan = '2' <br /> Alternate members: " +
    "<span class='white'>#############################</span>" + AlternatMember+"<br />"
    + "Weekly site cleaning: "+ 
    "<span class='white'>##########################</span>" + WeeklySiteCleaning +"<br />"+
     "Video surveillance: "+
     "<span class='white'>############################</span>" +VideoSurv +"<br />"+"<br />" +"</td>"
);
document.write("</tr>");


document.write("<tr>");

document.write("<td class='lefttext' colspan = '2' <br /> Site charges: " +
    "<span class='white'>#################################</span>" +
    cur2Format.format(SiteCost)+"<br />"
    +" Extra charges: "+  "<span class='white'>################################</span>" +
    cur2Format.format(ExtraChar) +"<br />"
);
document.write("</tr>");



document.write("<tr>");

document.write("<td class='lefttext' colspan = '2' <br /> Subtotal: " +
    "<span class='white'>####################################</span>" +
    
    cur2Format.format(SubTotal)+"<br />"
    +" Sales tax (HST): "+
    "<span class='white'>###############################</span>" +
      cur2Format.format(Hst) +"<br />"
);
document.write("</tr>");



document.write("<tr>");

document.write("<td class='lefttext' colspan = '2' <br /> Total monthly charges: " +
    "<span class='white'>##########################</span>" +
    cur2Format.format(TotalMonthly)+"<br />"
    +" Monthly dues: "+  
    "<span class='white'>################################</span>" +
    cur2Format.format(MonthlyDues) +"<br />"
);
document.write("</tr>");




document.write("<tr>");

document.write("<td class='lefttext' colspan = '2' <br /> Total monthly fees:" +
    "<span class='white'>############################</span>" +
    cur2Format.format(TotalMonthlyFees)+"<br />"
    +"Total yearly fees: "+  
    "<span class='white'>############################</span>" +
    cur2Format.format(TotalYearly) +"<br />"
);
document.write("</tr>");



document.write("<tr>");

document.write("<td class='lefttext' colspan = '2' <br /> Monthly payment:" +
    "<span class='white'>############################</span>" +
    cur2Format.format(MonthlyPayment)+"<br />"
);
document.write("</tr>");



document.write("<tr>");

document.write("<td class='lefttext' colspan = '2' <br /> Issued:" +
    "<span class='white'>###############################</span>" +
    CurDateStr+"<br />"
    +"HST Reg No: "+  
    "<span class='white'>##########################</span>" +
    randomFormattedNumber +"<br />"
    +"Cancellation fee: "+  
    "<span class='white'>###############################</span>" +
    cur2Format.format(cancellationFee) +"<br />"
);
document.write("</tr>");







document.write("</table>");

