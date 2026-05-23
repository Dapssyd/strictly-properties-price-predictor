# Deployment Guide | Property Price Prediction Engine

## 🏗️ Architecture
1. **Data Ingestion:** Historical transaction CSVs + CRM exports → SQL staging table
2. **Model Serving:** Flask REST API (`/predict`) wrapped around trained Ridge model
3. **Integration:** Embedded in internal CRM via iframe + AJAX call on property entry form
4. **Monitoring:** Weekly MAE tracking + drift detection on location/price distributions

```text
[Client Input] → CRM Form → Flask API (/predict) → Scikit-Learn Pipeline → JSON Response → CRM UI
       ↑                                          ↓
[Historical Data] → ETL Pipeline → Feature Store → Model Retraining (Quarterly)

## 🌐 API Example
```bash
curl -X POST http://internal-crm/predict \
  -H "Content-Type: application/json" \
  -d '{"location":"Lagos_Ikoyi", "space_sqm":150, "num_rooms":4, "num_bathrooms":3, "age":5}'

Response:
{"predicted_price_ngn": 85000000, "confidence_interval": [79.2M, 91.8M]}

## 🔗 Business Integration Workflow

   - Valuation officers enter property attributes into the internal CRM interface
   - Frontend sends an asynchronous POST request to /predict
   - Response populates the "Recommended Market Value" field within ~1.2s
   - Officers can add manual adjustments; all overrides are logged to improve future training data

## 📊 Monitoring & Maintenance

   - Performance Tracking: Weekly MAE/RMSE calculated against confirmed transaction prices
   - Drift Detection: Monthly distribution checks on key features (location mix, average space, age)
   - Retraining Cadence: Quarterly pipeline refresh using newly closed sales
   - Fallback Protocol: API latency >2s or missing features → triggers cached regional averages + manual review queue

## 🔒 Security & Compliance

   - No client PII or financial identifiers stored in model artifacts
   - API access restricted to internal network via IP allowlisting
   - Predictions include confidence bounds to support transparent client advisory
   - Portfolio Note: This guide documents a sanitized replica of the production system. Proprietary endpoints, internal CRM schemas, and authentication mechanisms have been generalized for academic portfolio purposes.
