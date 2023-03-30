/// <summary>
    /// Summary description for KenticoJSONTest
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // To allow this Web Service to be called from script, using ASP.NET AJAX, uncomment the following line. 
    [System.Web.Script.Services.ScriptService]
    public class AjaxWebService : System.Web.Services.WebService
    {

        [WebMethod]
        public string HelloWorld()
        {
            return "Hello World";
        }

        [WebMethod]
        [ScriptMethod(ResponseFormat = ResponseFormat.Json)]
        public String getState(string Country)
        {
            string retJSON = "";
            SqlConnection dbConn = new SqlConnection("<Connection String>");
            SqlDataAdapter dbAdapter = null;
            string sql = "SELECT STATE_FULL_NAME,STATE_SHORT_NAME FROM STATE WHERE COUNTRY LIKE '%" + Country + "%'";

            DataTable returnTable = new DataTable("State");
            dbConn.Open();
            dbAdapter = new SqlDataAdapter(sql, dbConn);
            dbAdapter.Fill(returnTable);
            dbConn.Close();

            retJSON = GetJson(returnTable);
            return retJSON;
        }


        private string GetJson(DataTable dt)
        {
            JavaScriptSerializer serializer = new JavaScriptSerializer();
            List<Dictionary<string, object>> rows =
              new List<Dictionary<string, object>>();
            Dictionary<string, object> row = null;

            foreach (DataRow dr in dt.Rows)
            {
                row = new Dictionary<string, object>();
                foreach (DataColumn col in dt.Columns)
                {
                    row.Add(col.ColumnName.Trim(), dr[col]);
                }
                rows.Add(row);
            }
            return serializer.Serialize(rows);
        }

    }
