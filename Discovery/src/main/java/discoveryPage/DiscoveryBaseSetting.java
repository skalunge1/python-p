package discoveryPage;

import java.util.concurrent.TimeUnit;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
 

public class DiscoveryBaseSetting {
	
 public WebDriver driver;
 static String driverPath = "";
 
 	
	public WebDriver getDriver() {
		return driver;
	}

	private void setDriver() {
		
			driver = initChromeDriver();
			
	}

	private static WebDriver initChromeDriver() {
		System.out.println("Launching google chrome with new profile..");
		System.setProperty("webdriver.chrome.driver", driverPath
				+ "chromedriver.exe");
		WebDriver driver = new ChromeDriver();
		driver.manage().window().maximize();
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		driver.get("https://www.discovery.com/");
		return driver;
	}

	
	
	@BeforeClass
	public void initializeTestBaseSetup() {
		System.out.println("initializeTestBaseSetup");
		try {
			setDriver();

		} catch (Exception e) {
			System.out.println("Error....." + e.getStackTrace());
		}
	}
	
	@AfterClass
	public void tearDown() {
		driver.quit();
	}
 
}
