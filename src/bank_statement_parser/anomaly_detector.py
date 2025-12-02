"""
Anomaly Detector Module

Detects anomalous transactions that may indicate fraud, money laundering,
or other suspicious activities.
"""

import numpy as np
from typing import List, Dict, Tuple
from .parser import Transaction


class AnomalyDetector:
    """
    Detect anomalous transactions using statistical methods.
    
    Identifies transactions that deviate significantly from normal patterns
    based on amount, frequency, and other features.
    """
    
    def __init__(self, threshold: float = 2.5):
        """
        Initialize anomaly detector.
        
        Args:
            threshold: Number of standard deviations to consider anomalous
        """
        self.threshold = threshold
        self.mean = None
        self.std = None
    
    def detect(self, transactions: List[Transaction]) -> List[Transaction]:
        """
        Detect anomalous transactions.
        
        Args:
            transactions: List of Transaction objects to analyze
            
        Returns:
            List of Transaction objects identified as anomalies
        """
        if not transactions:
            return []
        
        # Extract amounts
        amounts = [t.amount for t in transactions if t.amount is not None]
        
        if not amounts:
            return []
        
        # Calculate statistics
        self.mean = np.mean(amounts)
        self.std = np.std(amounts)
        
        # Identify anomalies
        anomalies = []
        for transaction in transactions:
            if self._is_anomaly(transaction):
                anomalies.append(transaction)
        
        return anomalies
    
    def _is_anomaly(self, transaction: Transaction) -> bool:
        """
        Check if a transaction is anomalous.
        
        Args:
            transaction: Transaction to check
            
        Returns:
            True if transaction is anomalous, False otherwise
        """
        if transaction.amount is None or self.mean is None or self.std is None:
            return False
        
        # Z-score method
        if self.std == 0:
            return False
        
        z_score = abs((transaction.amount - self.mean) / self.std)
        return z_score > self.threshold
    
    def get_anomaly_score(self, transaction: Transaction) -> float:
        """
        Calculate anomaly score for a transaction.
        
        Args:
            transaction: Transaction to score
            
        Returns:
            Anomaly score (higher = more anomalous)
        """
        if transaction.amount is None or self.mean is None or self.std is None:
            return 0.0
        
        if self.std == 0:
            return 0.0
        
        z_score = abs((transaction.amount - self.mean) / self.std)
        return z_score
    
    def analyze_patterns(self, transactions: List[Transaction]) -> Dict:
        """
        Analyze transaction patterns for suspicious activity.
        
        Args:
            transactions: List of transactions to analyze
            
        Returns:
            Dictionary containing pattern analysis results
        """
        anomalies = self.detect(transactions)
        
        results = {
            'total_transactions': len(transactions),
            'anomalies_detected': len(anomalies),
            'anomaly_rate': len(anomalies) / len(transactions) if transactions else 0,
            'threshold_used': self.threshold,
            'mean_amount': self.mean,
            'std_amount': self.std,
        }
        
        return results
    
    def generate_report(self, transactions: List[Transaction]) -> str:
        """
        Generate a report of anomaly detection results.
        
        Args:
            transactions: List of transactions analyzed
            
        Returns:
            Formatted string report
        """
        results = self.analyze_patterns(transactions)
        anomalies = self.detect(transactions)
        
        report = []
        report.append("=" * 50)
        report.append("Anomaly Detection Report")
        report.append("=" * 50)
        report.append(f"Total Transactions: {results['total_transactions']}")
        report.append(f"Anomalies Detected: {results['anomalies_detected']}")
        report.append(f"Anomaly Rate: {results['anomaly_rate']:.2%}")
        report.append(f"Detection Threshold: {results['threshold_used']} std devs")
        report.append(f"Mean Amount: ${results['mean_amount']:.2f}")
        report.append(f"Std Deviation: ${results['std_amount']:.2f}")
        report.append("=" * 50)
        
        if anomalies:
            report.append("\nTop Anomalies:")
            for i, transaction in enumerate(anomalies[:10], 1):
                score = self.get_anomaly_score(transaction)
                report.append(f"{i}. {transaction.description}: ${transaction.amount:.2f} (score: {score:.2f})")
        
        return "\n".join(report)
